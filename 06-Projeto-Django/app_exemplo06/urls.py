from django.urls import path

from app_exemplo06 import views

app_name = 'exemplo06'

urlpatterns = [
     path('', views.home, name='home')
]
