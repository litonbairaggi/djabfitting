from django import forms
from django.db import models
from django.forms import fields, widgets
from .models import Order

class OrderForm(forms.ModelForm):
    name = forms.CharField(label="Your Name", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Name Here'}), required=True, error_messages={'required':'Must Enter a Currect Name'})
    description = forms.CharField(label="Description", widget=forms.Textarea({'class': 'form-control', 'placeholder':'Description', 'rows':4, 'cols':50}), required=True, error_messages={'required':'Must Enter Descriptions'})
    class Meta:
        model = Order
        fields = '__all__'
        widgets = {
            'mobile': forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'Mobile Here'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'design': forms.Select(attrs={'class': 'form-check-input'}),
            'delivery': forms.Select(attrs={'class': 'form-check-input'}),
            'price':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Price'}),
            'payment':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Payment'}),
            'due':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Due'}),
            'received_date': forms.DateTimeInput(attrs={'class': 'form-control datetimepicker-input'}),
        }