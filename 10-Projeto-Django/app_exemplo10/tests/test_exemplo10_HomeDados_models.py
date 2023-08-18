from django.test import TestCase
from django.core.exceptions import ValidationError
from PIL import Image
from parameterized import parameterized
from app_exemplo10 import models


class Exemplo10HomeDadosModelsTestCase(TestCase):


    def setUp(self):
        dados = {
            'item1': 'Teste',
            'item2': 'Teste2',
            'item3': 'Teste3',
        }
        self.dados_banco = models.HomeDados.objects.create(**dados)
        self.dados_banco.full_clean()
        self.dados_banco.save()

    @parameterized.expand([
        ('item1', 5),
        ('item2', 10),
        ('item3', 15),
    ])
    def test_max_length_dos_campos(self, campo, max_length):
        setattr(self.dados_banco, campo, 'A' * (max_length + 1))

        with self.assertRaises(ValidationError):
            self.dados_banco.full_clean()

    def test_tamanho_da_imagem(self):
        self.dados_banco.imagem = 'teste.png'
        self.dados_banco.save()
        imagem = Image.open(self.dados_banco.imagem.path)

        self.assertLessEqual(imagem.width, 250)
        self.assertLessEqual(imagem.height, 250)

    def test_campo_imagem_defult(self):
        self.assertEqual(self.dados_banco.imagem, None)



    