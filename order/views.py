from django.shortcuts import render
from . models import Order
from .forms import OrderForm
# Create your views here.

def order(request):
    form = OrderForm()
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
    context = {
        'form':form
    }
    return render(request, 'order/create.html', context)    