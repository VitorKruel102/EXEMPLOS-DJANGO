from django.test import TestCase
from django.urls import resolve, reverse

from app_exemplo18 import views


class Exemplo18HomeViewsTestCase(TestCase):

    def test_views_esta_correta(self):
        url = reverse('exemplo18:home')
        view = resolve(url)

        self.assertEqual(view.func, views.home)

    def test_status_code_200(self):
        url = reverse('exemplo18:home')
        respota = self.client.get(url)

        self.assertEqual(respota.status_code, 200)