from unicodedata import decimal, name
from django.shortcuts import render
from django.views.generic import TemplateView, DeleteView, DetailView, CreateView, FormView
from . models import Cart, BookInCart, Order
from forecast.models import Book
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from . import forms


def get_cart(view):
    card_id = view.request.session.get("cart")
    if not card_id:
       if view.request.user.is_anonymous:
            customer = None
       else: 
            customer = view.request.user
            cart = Cart.objects.create (
            customer = customer)
            view.request.session["cart"] = cart.pk
    else: 
        cart = Cart.objects.get(pk=card_id)
    return cart

class AddToCart (TemplateView):
    template_name = "order\cart.html"
    
    def contact(request):
        form = forms.UserInfoForm()
        return render(request,
          'order/cart.html',
          {'form': form})

    def get_context_data(self, **kwargs):
        card_id = self.request.session.get("cart")
        book_id = self.request.GET.get ('book_id')
        try: 
            quantity = int(self.request.GET.get ('quantity'))
        except TypeError: 
            quantity = 0
        #1. get a cart 
        cart = get_cart(self)
        #2 Chek if the product-to-add-to-the cart was signaled
        #3. add a book to the cart
        book = Book.objects.get(pk=book_id)
        price = book.price * quantity
        #check if the book exist in cart
        book_in_cart, created = BookInCart.objects.get_or_create(
            cart = cart,
            book = book,
            defaults = {'quantity': quantity, 
            'price': price}
            )
        # update inf
        if not created: 
            book_in_cart.quantity = book_in_cart.quantity + quantity
            book_in_cart.price = book.price*book_in_cart.quantity
            book_in_cart.save()

        context = super().get_context_data(**kwargs)
        context['cart'] = cart
        return context
    
class DeleteFromCart (DeleteView):
    template_name = "order/delete_item.html"
    model =  BookInCart
    success_url = reverse_lazy('order:add_to_cart')

class UpdateCart(DetailView):
    template_name = "order/cart.html"
    model =  BookInCart

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def contact(request):
        form = forms.UserInfoForm()
        return render(request,
          'order/cart.html',
          {'form': form})
        
    def render_to_response(self, context, **response_kwargs):
        action_type = self.request.GET.get('action_type')
        if action_type == 'order':
            return HttpResponseRedirect('/main_page/thanks/')
        return super().render_to_response(context, **response_kwargs)

    def get_object(self, **kwargs):
        cart =  get_cart(self)
        book_price = 10.05
        form = forms.UserInfoForm
        for good in self.request.GET.keys():
            if good[:5] == "good_":
                good_in_cart_pk= int(good.split("__")[1])
                book_in_cart = BookInCart.objects.get(pk=good_in_cart_pk)
                book_in_cart.quantity = int(self.request.GET.get(good))
                book_in_cart.price = book_price*book_in_cart.quantity
                book_in_cart.save()
        action_type = self.request.GET.get('action_type')
        if action_type == 'order':
            order = Order.objects.create(
                    cart = book_in_cart.cart, 
                    name = self.request.GET.get("name"),
                    telephone=self.request.GET.get("telephone"),
                    address=self.request.GET.get("address"),
                    #desired_delivery_time =self.request.GET.get("desired_delivery_time"),
                )
            self.request.session.delete('cart')

        return cart

def contact(request):
    form = forms.UserInfoForm()
    return render(request,
        'order/info.html',
        {'form': form})

class ContactFormView(FormView):
    template_name = 'order/info.html'
    form_class = forms.UserInfoForm
    success_url = 'history.back()'