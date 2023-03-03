from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']

        username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'register-form'}))
        password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'register-form'}))
        password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'register-form'}))
        email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'register-form'}))


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'register-form'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'register-form'}))
