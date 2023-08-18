from django.test import SimpleTestCase

from django.urls import resolve, reverse
from app_exemplo09 import views

class Exemplo09HomeViewsTestCase(SimpleTestCase):


    def test_funcao_da_view_esta_correta(self):
        url = reverse("exemplo09:home")
        view = resolve(url)

        self.assertEqual(view.func, views.home)

    def test_retorno_status_code_200(self):
        url = reverse('exemplo09:home')
        resposta = self.client.get(url)

        self.assertEqual(resposta.status_code, 200)

    def test_template_esta_correto(self):
        url = reverse('exemplo09:home')
        resposta = self.client.get(url)

        self.assertTemplateUsed(resposta, 'app_exemplo09/pages/home.html')

    def test_retorno_do_exemplo_do_context(self):
        url = reverse('exemplo09:home')
        resposta = self.client.get(url)

        self.assertEqual(resposta.context['exemplo'], 'Testando aplicação')

    def test_context_exemplo_aparece_no_template(self):
        url = reverse('exemplo09:home')
        resposta = self.client.get(url)

        self.assertIn('Testando aplicação', resposta.content.decode('utf-8'))