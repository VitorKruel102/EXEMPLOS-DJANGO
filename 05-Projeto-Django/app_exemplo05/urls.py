from django.urls import path

from app_exemplo05 import views

app_name = 'exemplo05'

urlpatterns = [
    path('', views.home, name='home')
]
