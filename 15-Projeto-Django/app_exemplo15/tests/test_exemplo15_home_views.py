from django.test import TestCase
from django.urls import reverse, resolve

from app_exemplo15 import views, models


class Exemplo15HomeViewsTestCase(TestCase):


    def test_funcao_views_esta_correta(self):
        url = reverse('exemplo15:home')
        view = resolve(url)

        self.assertEqual(view.func, views.home)

    def test_status_code_200(self):
        url = reverse('exemplo15:home')
        resposta = self.client.get(url)

        self.assertEqual(resposta.status_code, 200)

    def test_template_esta_correto(self):
        url = reverse('exemplo15:home')
        resposta = self.client.get(url)

        self.assertTemplateUsed(resposta, 'exemplo15/pages/home.html')

    def test_produtos_esta_no_context(self):
        url = reverse('exemplo15:home')
        resposta = self.client.get(url)

        self.assertIn('produtos', resposta.context)


class Exemplo15HomeIntegrationTest(TestCase):


    def setUp(self):
        self.path_imagem = 'teste.png'
        self.dados_produtos = models.Produtos.objects.create(
            produto_01='Teste1',
            produto_02='Teste2',
            produto_03='Teste3',
            tipo='Tipo1',
            imagem=self.path_imagem
        )
        self.dados_produtos.full_clean()

    def test_se_tem_produtos_retornando_na_query(self):
        url = reverse('exemplo15:home')
        resposta = self.client.get(url)

        self.assertEqual(len(resposta.context['produtos']), 1)

    def test_produtos_aparece_no_template(self):
        url = reverse('exemplo15:home')
        resposta = self.client.get(url)

        self.assertIn('Teste1', resposta.content.decode('utf-8'))
        self.assertIn('Teste2', resposta.content.decode('utf-8'))
        self.assertIn('Teste3', resposta.content.decode('utf-8'))