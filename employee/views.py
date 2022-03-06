from django.shortcuts import render, get_object_or_404, redirect
from django.template import context
from . forms import EmployeeForm
from .models import Employee
from django.contrib import messages
# Create your views here.

# Create 
def create(request):
    form = EmployeeForm()
    if request.method == "POST":
        form =EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employee created')
            return redirect('employee_read')
    context = {
        'form':form
    }
    return render(request, 'employee/create.html', context)

# Read
def employee_read(request):
    employee_data = Employee.objects.all()
    context = {
        'employee_data': employee_data
    }
    return render(request, 'employee/read.html', context)