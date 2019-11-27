"""
This file contains all the user validation related code.

The 2 functions used are:
validate_login- Checks the password based on username and if it matches, accesses login
validate_registration- Checks if username/email id provided during registration are new or not. Also checks if password and confirmation passwords match.
"""

from website.models import User

def validate_login(username, password):
    """
    This function checks if the username entered during login is a valid one or not.
    It also checks if the password provided for the username matches or not.
    """
    user = User.objects.filter(username=username)
    if not user:
        return False
    passw = User.objects.filter(username=user[0].username, password=password)
    if passw:
        if passw[0].password == password :
            return True
    return False

def validate_registration(username, password1, password2, email):
    """
    This function checks during registration if the username and email id provided are new ones or not.
    It also checks if the 2 passwords provided match or not.
    """
    user = User.objects.filter(username=username)
    
    if user:
        print("user already exists")
        return False
    if password1 != password2 :
        print("password confirm not compatible")
        return False
    
    email = User.objects.filter(email=email)
    if email:
        print("email already exists")
        return False
    
    return True