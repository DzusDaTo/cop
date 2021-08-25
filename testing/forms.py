from .models import Test
from django.forms import ModelForm, TextInput


class TestForm(ModelForm):
    class Meta:
        model = Test
        fields = ['otvet1', 'otvet2', 'otvet3', 'otvet4', 'otvet5']

        widgets = {
            "otvet1": TextInput(attrs={
                'placeholder': 'ФИО'
            }),
            "otvet2": TextInput(attrs={
                'placeholder': 'Ответ 2'
            }),
            "otvet3": TextInput(attrs={
                'placeholder': 'Ответ 3'
            }),
            "otvet4": TextInput(attrs={
                'placeholder': 'Ответ 4'
            }),
            "otvet5": TextInput(attrs={
                'placeholder': 'Ответ 5'
            })
        }