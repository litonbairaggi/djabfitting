from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from category.models import Category
from order.models import Order
# Create your views here.

def home(request):
    total_category = Category.objects.count()
    total_order = Order.objects.count()
    # total_attendance = Attendance.objects.count()
    # total_designation = Designation.objects.count()
    # attend = Attendance.objects.all().order_by('-id')
    context = {
        'category': total_category,
        'order': total_order,
        # 'attendance': total_attendance,
        # 'designation': total_designation,
        # 'attend': attend
    }
    return render(request, 'home.html', context)