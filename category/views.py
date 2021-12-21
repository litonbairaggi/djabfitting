from django.shortcuts import render
from . forms import CategoryForm
# Create your views here.

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