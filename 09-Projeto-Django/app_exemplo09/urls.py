from django.urls import path

from app_exemplo09 import views

app_name = 'exemplo09'

urlpatterns = [
    path('', views.home, name='home')
]
