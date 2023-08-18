from django.test import TestCase
from django.urls import resolve, reverse

from app_exemplo18 import views


class Exemplo18HomeViewsTestCase(TestCase):

    def test_views_esta_correta(self):
        url = reverse('exemplo18:home')
        view = resolve(url)

        self.assertEqual(view.func, views.home)