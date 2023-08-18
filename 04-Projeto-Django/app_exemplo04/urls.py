from django.urls import path
from app_exemplo04 import views

app_name = 'exemplo_04'

urlpatterns = [
    path('', views.home, name='hone')
]
