from django.test import TestCase
from django.urls import resolve, reverse
from app_exemplo13 import views


class Exemplo13HomeViewsTesteCase(TestCase):


    def test_funcao_view_esta_correta(self):
        url = reverse('exemplo13:home')
        view = resolve(url)

        self.assertEqual(view.func, views.home)

    def test_retorno_status_200(self):
        url = reverse('exemplo13:home')
        resposta = self.client.get(url)

        self.assertEqual(resposta.status_code, 200)

    def test_carrega_template_correto(self):
        url = reverse('exemplo13:home')
        resposta = self.client.get(url)

        self.assertTemplateUsed(resposta, 'app_exemplo13/pages/home.html')

    def test_contem_exemplo13_no_context(self):
        url = reverse('exemplo13:home')
        resposta = self.client.get(url)

        self.assertIn('exemplo13', resposta.context)

    def test_aparece_exemplo_no_template(self):
        url = reverse('exemplo13:home')
        resposta =  self.client.get(url)

        self.assertIn('Exemplo13', resposta.content.decode('utf-8'))