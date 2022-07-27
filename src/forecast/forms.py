from django import forms
from datetime import datetime
from forecast import models

class CommentForm(forms.Form):
    name = forms.CharField(label='Your name')
    url = forms.URLField(label='Your feedback', required=False)
    comment = forms.CharField()
f = CommentForm(auto_id=False)
print(f)

class AddBookForm(forms.Form):
    genre=forms.ChoiceField(
        choices=models.Genre.GENRE_CHOICES, label = "Genre", required=True
    )
    name=forms.CharField (
        required=True,
        max_length=120,
        label = "Name"
    )
    authors=genre=forms.MultipleChoiceField(
        choices=models.Author.objects.all,
        label = "Authors", 
        required=True
    )
    publisher=forms.CharField (
        required=True,
        max_length=120,
        label = "Publisher"
    )
    #seria=forms.MultipleChoiceField(
        #seria=models.Seria.objects.all(),
        #label = "Seria", 
        #required=True
    #)
    date=forms.DateField(
        required=True,
        widget=forms.SelectDateWidget,
        label = "Date"
    )
    description=forms.CharField(
        widget=forms.Textarea,
        required=False,
        label = "Description"
    )