from django.test import TestCase
from django.core.exceptions import  ValidationError
from django.conf import settings

from app_exemplo18 import models

from parameterized import parameterized


class Exemplo18ProdutosModelsTestCase(TestCase):

    def setUp(self):
        self.path_imagem = 'teste.png'
        dados_produtos = {
            'titulo': 'Titulo Teste',
            'descricao': 'Testando descrição',
            'categoria': 'Roupa M',
            'imagem_produto': self.path_imagem
        }

        self.produto = models.Produtos.objects.create(**dados_produtos)
        self.produto.full_clean()

    def test_max_length_do_campo_titulo(self): 
        self.produto.titulo = 'A' * (50 + 1)

        with self.assertRaises(ValidationError):
            self.produto.full_clean()

    def test_quantidade_de_categorias(self):
        self.assertEqual(len(models.Produtos.CATEGORIAS), 5)

    @parameterized.expand([
        ('Roupa M'),
        ('Roupa F'),
        ('Carros'),
        ('Motos'),
        ('Casa'),
    ])
    def test_cadastrando_categorias_corretas(self, valores):
        self.produto.categoria = valores
        self.produto.full_clean()

    def test_cadastrando_categoria_incorreta(self):
        self.produto.categoria = 'Teste Categoria'

        with self.assertRaises(ValidationError):
            self.produto.full_clean()

    def test_max_size_para_as_imagens(self):
        self.assertEqual(models.Produtos.MAX_SIZE, (250, 250))

    def test_metodo_str(self):
        self.assertEqual(str(self.produto), self.produto.titulo)

    def test_verbose_name_plural(self):
        verbose_name_plural = models.Produtos._meta.verbose_name_plural

        self.assertEqual(verbose_name_plural, 'Produto')