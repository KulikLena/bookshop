from django import forms
from django.db import models
from datetime import datetime
from forecast import models

#class CommentForm(forms.Form):
#   name = forms.CharField(label='Your name')
#    url = forms.URLField(label='Your feedback', required=False)
#    comment = forms.CharField()
#f = CommentForm(auto_id=False)
#print(f)

class AddBookForm(forms.Form):
    genre=forms.ChoiceField(
        choices=models.Genre.GENRE_CHOICES, label = "Genre", required=True
    )
    name=forms.CharField (
        required=True,
        max_length=120,
        label = "Name"
    )
    authors=forms.MultipleChoiceField(
        choices=models.Author.objects.all,
        label = "Authors", 
        required=True
    )
    price=forms.IntegerField(
        required=True,
        label = "Price"
    )

    publisher=forms.CharField (
        required=True,
        max_length=120,
        label = "Publisher"
    )
    seria = forms.ChoiceField(
        choices=models.Seria.objects.all,
        label = "Seria", 
        required=False
    )
   
    date=forms.DateField(
        required=True,
        widget=forms.SelectDateWidget,
        label = "Date"
    )

    pages=forms.IntegerField(
        required=True,
        label = "Pages"
    )
    cover=forms.ChoiceField(
        choices=models.Cover.COVER_CHOICES, label = "Cover", required=True
    )

    format= forms.CharField (
            label = "Format",
            help_text="Please use the following format: width(cm) x length(cm): "
    )

    #format= forms.MultiValueField (
    #    fields=(forms,forms.IntegerField(label = 'width(cm)'), forms.IntegerField(label = 'length(cm)')),
    #    label = "Format",
    #    error_messages = "Incomplete"
    #)

    seria = forms.ChoiceField(
        choices=models.Seria.objects.all,
        label = "Authors", 
        required=True
    )
    
    description=forms.CharField(
        widget=forms.Textarea,
        required=False,
        label = "Description"
    )