from django.urls import path

from App_exemplo03 import views

app_name = 'exemplo03'

urlpatterns = [
    path('', views.home, name='home')
]
