from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('create/', views.create, name="create"),
    path('', views.employee_read, name='employee_read'),
    path('<int:pk>/', views.employee_update, name='employee_update'),
    # path('delete/<int:pk>/', views.category_delete, name='category_delete'),   
]