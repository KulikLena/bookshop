from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from random import randint
from forecast import forms


from requests import post
from . import models 

from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView, CreateView, DeleteView

# Create your views here.
def show_forecast_view(request):
    NAMES = (request.user, 'Nik', 'Mike', 'Rosenkranz', 'Güldenstern') 
    username=NAMES[randint(0,4)]
    PREDICTIONS =('The night is dark and full of terrors','So long, and thanks for all the fish', 
                   'Don_t Panic', 'Something is rotten in the state of Denmark')
    forecast=PREDICTIONS[randint(0,3)]
    return HttpResponse (f"<h1>{forecast}, {username} </h1>")

#def show_mainpage_view(request):
#    out='<ul>'
#    books=models.Book.objects.all()
#   for bk in books: 
#       out += f"<li> Book {bk.id}  was first published in {bk.first_published} </li>"
#   out+='</ul>'
 #   return HttpResponse('In model Book will be placed unique instances of books in case some books could have several editions in different languages')

def book_add_view(request):
    if request.method == 'POST':
        form=forms.AddBookForm(request.POST)
        if form.is_valid():    
            book=models.Book.objects.create(
            genre=form.cleaned_data('genre'),
            name=form.cleaned_data('name'),
            authors=form.cleaned_data('authors'),
            publisher=form.cleaned_data('publisher'),
            date=form.cleaned_data('date'),
            description=form.cleaned_data('description'),
        )
            return HttpResponseRedirect('book/{book.id}>/')
        else:
            print("Form is not valid!") 



    elif request.method == 'GET':
        form = forms.AddBookForm()
        return render(request='forecast/book_add.html',context={'form':form})

class MapPage(TemplateView):
    template_name='forecast/map.html'
    

class BookPage(ListView):
    template_name='forecast/books_list.html'
    model=models.Book
    def get_queryset(self):
        qs=self.model.objects.all()
        return qs
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context

class BookDetailView(DetailView):
    template_name='forecast/book_view.html'
    model=models.Book

class BookAdd(CreateView):
    template_name='forecast/book_add.html'
    model=models.Book
    fields = '__all__'
    def get_success_url(self):
        return f'book/{object.id}'


class DeleteBook(DeleteView):
    template_name='forecast/book_delete.html'
    model=models.Book
    def get_success_url(self):
        return f'book/{object.id}'

class MainPage(TemplateView):
    template_name='forecast/main_page.html'