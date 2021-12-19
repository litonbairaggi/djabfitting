from django import forms
from django.db import models
from django.forms import fields, widgets
from .models import Category, Order

class CategoryForm(forms.ModelForm):
    category_name = forms.CharField(label="Category Name", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Category Name'}), required=True, error_messages={'required':'Must Enter a Currect Name'})
    class Meta:
        model = Category
        fields = '__all__'