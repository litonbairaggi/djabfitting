from django.shortcuts import render
from . forms import CategoryForm
# Create your views here.

def category(request):
    form = CategoryForm()
    context = {
        'form':form
    }
    return render(request, 'category/create.html')