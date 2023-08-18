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
        resposta = self.client.get(url)

        self.assertEqual(resposta.status_code, 200)

    def test_template_esta_correto(self):
        url = reverse('exemplo18:home')
        resposta = self.client.get(url)

        self.assertTemplateUsed(resposta, 'app_exemplo18/pages/home.html')