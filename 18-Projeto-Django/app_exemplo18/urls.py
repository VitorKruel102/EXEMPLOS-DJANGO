from django.urls import path

from app_exemplo18 import views

app_name = 'exemplo18'

urlpatterns = [ 
    path('', views.home, name='home'),
]
