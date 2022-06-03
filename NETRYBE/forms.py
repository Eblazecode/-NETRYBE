 from django import forms
from django import forms
from .models import Post

class contactform(forms.Form):
    firstname = forms.CharField(max_length=100)
    Email = forms.CharField( max_length=200)
    phonenum = forms.CharField(max_length=15)

