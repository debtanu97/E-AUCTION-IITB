"""
File which stores all the forms.
"""

from django import forms
from .models import *

class RegistrationForm(forms.Form):
    """
    Stores the user credentials upon first time registration.

    """
    username = forms.CharField(max_length=45)
    email = forms.EmailField()
    password1 = forms.CharField(max_length=45)
    password2 = forms.CharField(max_length=45)
    firstname = forms.CharField(max_length=56)
    lastname = forms.CharField(max_length=45)
    cellphone = forms.CharField(max_length=45)
    address = forms.CharField(max_length=255)
    town = forms.CharField(max_length=45)
    postcode = forms.CharField(max_length=45)
    country = forms.CharField(max_length=45)

class LoginForm(forms.Form):
    """
    Inputs user id and password during login.
    """
    username = forms.CharField(max_length=45)
    password = forms.CharField(max_length=45)

class TopUpForm(forms.Form):
    """
    Dropdown menu for available topup amounts.
    """ 
    amount = forms.DecimalField(max_digits=7, decimal_places=2)

class CommentForm(forms.Form):
    """
    Box where user can comment on a product.
    """ 
    comment = forms.CharField(widget=forms.Textarea)

class PutUpAuctionForm(forms.Form):
    """
    Inputs new product details from user for auction.
    """ 
    title = forms.CharField(max_length=45)
    description = forms.CharField(max_length=200)
    time_starting = forms.DateField()
    hour_starting = forms.IntegerField()
    base_price = forms.IntegerField(max_value=200000, min_value=10)
    duration = forms.IntegerField(max_value=20, min_value=1)
    category = forms.CharField(max_length=2)
    image = forms.ImageField()

