from django.urls import path
from app_exemplo07 import views

app_name = 'exemplo07'

urlpatterns = [
    path('', views.home, name='home')
]
