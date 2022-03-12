from django.db import models
from django.utils.timezone import now
from category.models import Category
from employee.models import Employee

class Order(models.Model):
    name = models.CharField(max_length=64, null=True, blank=True)
    mobile = models.IntegerField(null=True, blank=True, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False)
    DESIGNS = (
        ('', 'Select'),
        ('narrow fitting', 'narrow fitting'),
        ('Slim Fit', 'Slim Fit'),
    )
    design = models.CharField(max_length=100, null=True, blank=True, choices=DESIGNS)
    description = models.TextField(max_length=700, null=True, blank=True)
    DELIVERYS = (
        ('', 'Select'),
        ('Normal', 'Normal'),
        ('Urgent', 'Urgent'),
    )
    delivery = models.CharField(max_length=100, null=True, blank=True, choices=DELIVERYS)
    price = models.PositiveIntegerField(blank=False)
    payment = models.PositiveIntegerField(blank=True)
    received_date = models.DateTimeField()
    due = models.PositiveIntegerField(blank=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=False)
    created_date = models.DateTimeField(default=now)