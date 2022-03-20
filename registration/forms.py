from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class MyForm(UserCreationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={
                'class': 'form-control-registr',
                'placeholder': 'Имя пользователя'}))
    email = forms.EmailField(label='', max_length=200, widget=forms.TextInput(attrs={
                'class': 'form-control-registr',
                'placeholder': 'E-mail'}))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={
                'class': 'form-control-registr',
                'placeholder': 'Пароль'}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={
        'class': 'form-control-registr',
        'placeholder': 'Повторите пароль'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя пользователя'}),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'E-mail'}),
            }
# class UserAuthForm(AuthenticationForm):
#     username = forms.CharField(label='', widget=forms.TextInput(attrs={
#         'class': 'form-control-registr',
#         'placeholder': 'Имя пользователя'}))
#     password = forms.CharField(label='', widget=forms.PasswordInput(attrs={
#         'class': 'form-control-registr',
#         'placeholder': 'Пароль'}))