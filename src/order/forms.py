from django import forms
from django.db import models
from datetime import datetime
from forecast import models

MORNING = '10am - 5pm'
EVENING ='5pm - 10pm'

class UserInfoForm(forms.Form):

    name=forms.CharField (
        required=True,
        max_length=120,
        label = "Name")

    telephone=forms.CharField (
        required=True,
        max_length=13,
        label = "Telephone")

    address=forms.CharField (
        required=True,
        max_length=140,
        label = "Addresse")

    desired_delivery_time=forms.ChoiceField(
        choices=[(MORNING,'10am - 5pm'), (EVENING, '5pm - 10pm')],
        label = "Desired delivery time", 
        required=True)

   



