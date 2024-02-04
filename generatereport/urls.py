from django.urls import path
from . import views
from .views import generate_csv

urlpatterns = [
    path('', views.index, name='report'),
    path('generate_csv/', generate_csv, name='generate_csv'),
]