from django.test import TestCase
from django.urls import resolve, reverse

from app_exemplo10 import views


class Exemplo10HomeViewsTestCase(TestCase):


    def setUp(self):
        self.url = reverse('exemplo10:home')
        self.resposta_get = self.client.get(self.url)

    def test_funcao_view_esta_correta(self):
        view = resolve(self.url)

        self.assertEqual(view.func, views.home)

    def test_status_code_retorna_200(self):
        self.assertEqual(self.resposta_get.status_code, 200)

    def test_template_esta_correto(self):
        self.assertTemplateUsed(self.resposta_get, 'app_exemplo10/pages/home.html')

    def test_retorno_do_exemplo_no_context(self):
        exemplo_context = self.resposta_get.context['exemplo']

        self.assertEqual(exemplo_context, 'Testando context')

    def test_exemplo_context_aparece_no_template(self):
        template_atual = self.resposta_get.content.decode('utf-8')

        self.assertIn('Testando context', template_atual)