from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegiesterForm(UserCreationForm):
    # username, pw and pwconfirm is already there
    email = forms.EmailField(required=True)

    # kind of a config?
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
