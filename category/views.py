from django.shortcuts import render
from . forms import CategoryForm
from .models import Category
# Create your views here.

# Create 
def category(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
    context = {
        'form':form
    }
    return render(request, 'category/create.html', context)

# Read
def read(request):
    category_data = Category.objects.all()
    context = {
        'category_data': category_data
    }
    return render(request, 'category/read.html', context)