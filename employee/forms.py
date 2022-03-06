from django import forms
from django.db import models
from django.forms import fields, widgets
from .models import Employee

class EmployeeForm(forms.ModelForm):
    employee_name = forms.CharField(label='Employee Name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Employee Name'}), required=True, error_messages={'required':'Must Enter a Correct Name'})
    class Meta:
        model = Employee
        fields = ['id', 'employee_name']