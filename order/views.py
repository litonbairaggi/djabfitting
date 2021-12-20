from django.shortcuts import render
from . models import Order
from .forms import OrderForm
# Create your views here.

def order(request):
    form = OrderForm()
    context = {
        'form':form
    }
    return render(request, 'order/create.html', context)    