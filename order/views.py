from django.shortcuts import get_object_or_404, redirect, render
from . models import Order
from django.contrib import messages
from .forms import OrderForm
# Create your views here.

# Create
def create(request):
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

# Update
def update(request, pk):
    get_data = get_object_or_404(Order, pk=pk)
    form = OrderForm(instance=get_data)
    if request.method == "POST":
        form = OrderForm(request.POST, instance=get_data)
        if form.is_valid():
            form.save()
            messages.success(request, 'Order updated')
            return redirect(request, 'reade')
    context = {
        'form': form
    }        
    return render(request, 'order/create.html', context)