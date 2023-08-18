from django.urls import path

from . import views

app_name = 'exemplo02'

urlpatterns = [
    path('', views.home, name='home')    
]
