from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import TextInput, EmailInput, PasswordInput


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Ник', widget=TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=PasswordInput(attrs={'class': 'form-control'}))


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Ник', widget=TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='Имя', widget=TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Фамилия', widget=TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(label='Email', widget=EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Подтвердите пароль', widget=PasswordInput(attrs={'class': 'form-control'}))
    school_number = forms.CharField(label='Название школы и №', widget=TextInput(attrs={'class': 'form-control'}))
    age = forms.CharField(label='Возраст', widget=TextInput(attrs={'class': 'form-control'}))
    grade = forms.CharField(label='Класс', widget=TextInput(attrs={'class': 'form-control'}))
    parenst = forms.CharField(label='ФИО родителя', widget=TextInput(attrs={'class': 'form-control'}))
    number_parenst = forms.CharField(label='Телефон родителя', widget=TextInput(attrs={'class': 'form-control'}))

    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'school_number', 'age', 'grade', 'parenst', 'number_parenst')
        widgets = {
            "username": TextInput(),
            "first_name": TextInput(),
            "last_name": TextInput(),
            "email": EmailInput(),
            "password1": PasswordInput(),
            "password2": PasswordInput(),
            "school_number": TextInput(),
            "age": TextInput(),
            "grade": TextInput(),
            "parenst": TextInput(),
            "number_parenst": TextInput()
        }

