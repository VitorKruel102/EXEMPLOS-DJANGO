from django.urls import path
from . import views

app_name = 'exemplo01'

urlpatterns = [
    path('', views.home, name='home')
]