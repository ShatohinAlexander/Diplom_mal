from django import forms
from .models import Pet, Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'phone', 'animal']
        labels = {
            'name': 'Ваше имя',
            'phone': 'Номер телефона',
            'animal': 'Выберите животное'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите ваше имя'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'id':'phone', 'placeholder': 'Введите номер телефона'}),
            'animal': forms.Select(attrs={'class': 'form-control'})
        }
