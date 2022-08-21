from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from random import randint
from forecast import forms
from requests import post
from . import models 
from django.views.generic import ListView, TemplateView, DetailView, CreateView, DeleteView


def show_forecast_view(request):
    NAMES = (request.user, 'Nik', 'Mike', 'Rosenkranz', 'Güldenstern') 
    username=NAMES[randint(0,4)]
    PREDICTIONS =('The night is dark and full of terrors','So long, and thanks for all the fish', 
                   'Don_t Panic', 'Something is rotten in the state of Denmark')
    forecast=PREDICTIONS[randint(0,3)]
    return HttpResponse (f"<h1>{forecast}, {username} </h1>")

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    

class BookAdd(CreateView):
    template_name='forecast/book_add.html'
    model=models.Book
    fields = '__all__'
    def get_success_url(self):
        return f'book/{object.pk}'


class DeleteBook(DeleteView):
    template_name='forecast/book_delete.html'
    model=models.Book
    def get_success_url(self):
        return f'book/{object.pk}'

class MainPage(ListView):
    template_name='forecast/main_page.html'
    model=models.Book
    def get_queryset(self):
        qs=self.model.objects.all()
        return qs
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context


class NavBar(TemplateView):
    template_name='forecast/navbar.html'

class BookSearch(ListView):
    template_name='forecast/books_search.html'
    model=models.Book
    def get_queryset(self):
        q=self.request.GET.get('search_query')
        if q: 
            qs = self.model.objects.filter(name__contains = q)
        else: 
            qs = []
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context

class NewArrivals(ListView):
    template_name='forecast/new_arrivals.html'
    model=models.Book
    def get_queryset(self):
        qs=self.model.objects.all()
        return qs
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context

class Bestsellers(ListView):
    template_name='forecast/bestsellers.html'
    model=models.Book
    def get_queryset(self):
        qs=self.model.objects.all()
        return qs
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context

class Catalogue(ListView):
    template_name='forecast/catalogue.html'
    model=models.Book
    def get_queryset(self):
        qs=self.model.objects.all()
        return qs
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context