from django.test import TestCase
from django.urls import reverse, resolve

from app_exemplo12 import views


class Exemplo12HomeViewsTestCase(TestCase):


    def test_funcao_da_view_esta_correta(self):
        url = reverse('exemplo12:home')
        view = resolve(url)

        self.assertEqual(view.func, views.home)

    def test_status_code_200(self):
        url = reverse('exemplo12:home')
        resposta = self.client.get(url)

        self.assertEqual(resposta.status_code, 200)

    def test_se_carrega_template_correto(self):
        url = reverse('exemplo12:home')
        resposta = self.client.get(url)

        self.assertTemplateUsed(resposta, 'app_exemplo12/pages/home.html')

    def test_se_existe_exemplo12_no_context(self):
        url = reverse('exemplo12:home')
        resposta = self.client.get(url)

        self.assertIn('exemplo12', resposta.context)