from django.urls import path

from app_exemplo13 import views

app_name = 'exemplo13'

urlpatterns = [
    path('', views.home, name='home'),
]
