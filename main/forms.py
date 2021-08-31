from .models import Shipment
from django.forms import ModelForm, TextInput


class ShipmentForm(ModelForm):
    class Meta:
        model = Shipment
        fields = ['last_name', 'first_name', 'Email', 'school', 'age', 'grade', 'fio', 'number_fio']
        widgets = {
            "last_name": TextInput(attrs={'class':'form-control', 'placeholder': 'Фамилия'}),
            "first_name": TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'}),
            "Email": TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            "school": TextInput(attrs={'class': 'form-control', 'placeholder': 'Название школы и №'}),
            "age": TextInput(attrs={'class': 'form-control', 'placeholder': 'Возраст'}),
            "grade": TextInput(attrs={'class': 'form-control', 'placeholder': 'Класс'}),
            "fio": TextInput(attrs={'class': 'form-control', 'placeholder': 'ФИО родителя'}),
            "number_fio": TextInput(attrs={'class': 'form-control', 'placeholder': 'Телефон роителя'}),
        }