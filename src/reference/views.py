from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView, CreateView, DeleteView
from django.urls import reverse_lazy
from reference import models
from forecast import forms

class AuthorDetail(DetailView):
    template_name = "reference/item_detail.html"
    model = models.Author
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class AuthorAdd(CreateView):
    model = models.Author
    template_name = 'reference/item_add.html'
    fields = '__all__'
      
    def get_success_url(self):
        
        #reverse_lazy("auth-add", kwargs={'id': self.object.pk})
        return f"/ref/auth/add/{self.object.pk}/"

class PublisherDetail(DetailView):
    template_name = "reference/item_detail.html"
    model = models.Publisher

class PublisherAdd(CreateView):
    model = models.Publisher
    template_name = 'reference/item_add.html'
    fields = '__all__'
    
    def get_success_url(self):
        #reverse_lazy("pub-add", kwargs={'id': self.object.id})
        return f"/ref/pub/add/{self.object.pk}/"

class AuthorList(ListView):
    template_name = "reference/item_list.html"
    model = models.Author

class PublisherList(ListView):
    template_name = "reference/item_list.html"
    model = models.Publisher