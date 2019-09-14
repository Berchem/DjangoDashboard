from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={"autofocus": "", "class": "form-control", "placeholder": "Username"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password confirmation"}))
    # first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    # last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.',
                             widget=forms.TextInput(
                                 attrs={"autofocus": "", "class": "form-control", "placeholder": "E-mail"})
                             )

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email', )
        # fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
