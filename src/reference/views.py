from django.shortcuts import render
from django.views import generic
from . import models
from forecast import forms

class AuthorDetail(generic.DetailView):
    template_name = "reference/item_detail.html"
    model = models.Author

class AuthorAdd(generic.CreateView):
    template_name = "reference/item_edit.html"
    fields =['first_name' , 'last_name', 'birth_date', 'death_date', 'country_of_birth', 'description']
    model = models.Author