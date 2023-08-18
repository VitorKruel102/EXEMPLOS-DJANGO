from django.urls import path
from app_exemplo15 import views

app_name = 'exemplo15'

urlpatterns = [
    path('', views.home, name='home'),
    path('', views.register_create, name='create')
]
