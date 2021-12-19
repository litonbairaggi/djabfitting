from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import Order

# Register your models here.

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['name', 'mobile', 'category', 'design', 'description', 'delivery', 'price', 'payment', 'received_date', 'due']
