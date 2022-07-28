from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from . import models
from forecast import forms

class AuthorDetail(generic.DetailView):
    template_name = "reference/item_detail.html"
    model = models.Author

class AuthorAdd(generic.CreateView):
    template_name = "reference/item_edit.html"
    fields =['first_name' , 'last_name', 'birth_date', 'death_date', 'country_of_birth', 'description']
    model = models.Author

    def get_success_url(self):
        reverse_lazy("auth-add", kwargs={'id': self.object.id})
        #return f"/ref/auth/{self.object.pk}/"

class PublisherDetail(generic.DetailView):
    template_name = "reference/item_detail.html"
    model = models.Publisher

class PublisherAdd(generic.CreateView):
    template_name = "reference/item_edit.html"
    fields =['publisher_name' , 'country', 'description']
    model = models.Publisher

    def get_success_url(self):
        reverse_lazy("pub-add", kwargs={'id': self.object.id})
        #return f"/ref/pub/{self.object.pk}/"