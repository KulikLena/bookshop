from django import forms
from django.db import models
from datetime import datetime
from forecast import models

class AddBookForm(forms.Form):

    name=forms.CharField (
        required=True,
        max_length=120,
        label = "Name")

    authors=forms.MultipleChoiceField(
        choices=models.Author.objects.all,
        label = "Authors", 
        required=True)

    price=forms.IntegerField(
        required=True,
        label = "Price")

    publisher=forms.CharField (
        required=True,
        max_length=120,
        label = "Publisher")
    #seria = forms.ChoiceField(
    #    choices=models.Seria.objects.all,
    #    label = "Seria", 
    #    required=False
    #)
    genre=forms.ChoiceField(
        choices=models.Genre.GENRE_CHOICES, label = "Genre", required=True)
   
    date_published=forms.DateField(
        required=True,
        widget=forms.SelectDateWidget,
        label = "Date published")

    pages=forms.IntegerField(
        required=True,
        label = "Pages")

    cover=forms.ChoiceField(
        choices=models.Cover.COVER_CHOICES, label = "Cover", required=True)

    format= forms.CharField (
            label = "Format",
            help_text="Please use the following format: width(cm) x length(cm): ")

    #format= forms.MultiValueField (
    #   fields=(forms, forms.IntegerField(label = 'width(cm)'), forms.IntegerField(label = 'length(cm)')),
    #   label = "Format",
    #   error_messages = "Incomplete")

    isbn= forms.CharField (
            label = "ISBN",
            help_text="Please use the following format: 000-000-0000-00-0' ")

    weight=forms.IntegerField(
        required=True,
        label = "Weight")
    
    cover=forms.ChoiceField(
        choices=models.Cover.COVER_CHOICES, label = "Cover", required=True)

    age_restriction=forms.ChoiceField(
        choices=models.AgeRestriction.AGE_RESTRICT_CHOICES, label = "Age restrictions", required=True)

    items_available=forms.IntegerField(
        required=True,
        label = "Items available")

    order_status=forms.ChoiceField(
        choices=[(models.ACTIVE,'Active'), (models.INACTIVE,'Inactive')],
        label = "Order choises", 
        required=True)

    rate=forms.DecimalField (
        required=False,
        label = "Items available")

    description=forms.CharField(
        widget=forms.Textarea,
        required=False,
        label = "Description")

class BookSearchForm(forms.Form):
    search_text =  forms.CharField(
        required = False,
        label='Search by name',
        widget=forms.TextInput(attrs={'placeholder': 'search here!'})
    )



