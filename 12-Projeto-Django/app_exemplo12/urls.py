from django.urls import path

from app_exemplo12 import views

app_name = 'exemplo12'

urlpatterns = [
    path('', views.home, name='home'),
]
