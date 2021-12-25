from django.shortcuts import redirect, render
from . models import Order
from django.contrib import messages
from .forms import OrderForm
# Create your views here.

def order(request):
    form = OrderForm()
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Order created')
            return redirect('read')
    context = {
        'form':form
    }
    return render(request, 'order/create.html', context)    


# Read
def read(request):
    order_data = Order.objects.all()
    context = {
        'order_data': order_data
    }
    return render(request, 'order/read.html', context)
