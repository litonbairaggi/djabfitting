from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('create/', views.create, name="create"),
    path('', views.read, name='read'),
    path('<int:pk>/', views.update, name='update'),
    path('delete/<int:pk>/', views.delete, name='delete'),   
]