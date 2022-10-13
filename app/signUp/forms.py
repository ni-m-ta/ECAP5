from django import forms
from django.contrib.auth.models import User
from .models import Account


# To create a form class
class AccountForm(forms.ModelForm):
    # To put password
    password = forms.CharField(widget=forms.PasswordInput(), label="Password")

    class Meta():
        # To verify users
        model = User
        # To assign a field
        fields = ('username', 'email', 'password')
        # To assign a field name
        labels = {'username': "userID", 'email': "Email"}


class AddAccountForm(forms.ModelForm):
    class Meta():
        # To assign a model class
        model = Account
        fields = ('first_name', 'last_name', )
        labels = {'first_name': "First Name", 'last_name': "Last Name", }
