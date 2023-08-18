from django.test import TestCase
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile

from PIL import Image
from parameterized import parameterized
from app_exemplo13.models import ItensProdutos


class Exemplo13ItensProdutosModelsTestCase(TestCase):


    def setUp(self):
        self.path_imagem = 'teste.png'
        self.dados_models = ItensProdutos(item1='Pão', tipo='I1', imagem=self.path_imagem)
        self.dados_models.full_clean()

    @parameterized.expand([
        ('item1', 25),
        ('tipo', 2),
    ])
    def test_campos_com_max_length(self, campo, max_length):
        novo_item = 'A' * (max_length + 1)
        setattr(self.dados_models, campo, novo_item)

        with self.assertRaises(ValidationError):
            self.dados_models.full_clean()

    def test_tamanho_maximo_da_imagem(self):
        _imagem = Image.open(self.dados_models.imagem.path)

        self.assertLessEqual(_imagem.width, 800)
        self.assertLessEqual(_imagem.height, 800)

    def test_erro_ao_registrar_um_tipo_incorreto(self):
        self.dados_models.tipo = 'Item Errado'

        with self.assertRaises(ValidationError):
            self.dados_models.full_clean()

    @parameterized.expand([
        ('I1'),
        ('I2'),
        ('I3'),
    ])
    def test_registrando_tipos_corretor(self, valor):
        self.dados_models.tipo = valor
        self.dados_models.full_clean()

    def test_quantidade_de_itens_no_choices(self):
        self.assertEqual(len(self.dados_models.CHOICE_TIPOS), 3)

    def test_retorno_do_metodo_str(self):
        self.assertEqual(str(self.dados_models), 'Pão')

    def test_path_vazio_se_nao_for_enviado_a_imagem(self):
        self.dados_models.imagem = ''
        self.dados_models.save()

        path_imagem = self.dados_models.imagem

        self.assertFalse(path_imagem)

    def test_tamanho_maximo_da_imagem_esta_correta(self):
        self.assertEqual(self.dados_models.max_size, (800, 800))

