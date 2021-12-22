from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('create/', views.category, name="create"),
    path('', views.read, name="read"),
]