from django.urls import path
from app_exemplo10 import views

app_name = 'exemplo10'

urlpatterns = [
    path('', views.home, name='home')
]
