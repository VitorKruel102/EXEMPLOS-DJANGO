from django.test import TestCase
from django.core.exceptions import ValidationError
from django.urls import reverse

from parameterized import parameterized
from app_exemplo15.models import Produtos


class ProdutosModelsTestCase(TestCase):


    def setUp(self):
        self.path_imagem = 'teste.png'
        self.dados_produtos = Produtos.objects.create(
            produto_01='ProdutoTeste1',
            produto_02='ProdutoTeste2',
            produto_03='ProdutoTeste3',
            tipo='Tipo1',
            imagem=self.path_imagem,
        )   
        self.dados_produtos.full_clean()

    @parameterized.expand([
        ('produto_01', 25),
        ('produto_02', 25),
        ('produto_03', 25),
        ('tipo', 5),
    ])
    def test_campos_max_length(self, campo, max_length):
        novo_valor = 'A' * (max_length + 1)
        setattr(self.dados_produtos, campo, novo_valor)

        with self.assertRaises(ValidationError):
            self.dados_produtos.full_clean()

    @parameterized.expand([
        ('Tipo1'),
        ('Tipo2'),
        ('Tipo3'),
    ])
    def test_adicionando_tipos_correstos(self, valor_tipo):
        self.dados_produtos.tipo = valor_tipo
        self.dados_produtos.full_clean()

    def test_quantidade_de_itens_no_choice(self):
        self.assertEqual(len(Produtos.TIPOS_CHOICES), 3)

    def test_metodo_str(self):
        self.assertEqual(str(self.dados_produtos), 'Tipo1')