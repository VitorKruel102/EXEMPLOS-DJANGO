from django.db import models
from PIL import Image


class Produtos(models.Model):
    MAX_SIZE = (100, 100)
    TIPOS_CHOICES = (
        ('Tipo1', 'Tipo 1'),
        ('Tipo2', 'Tipo 2'),
        ('Tipo3', 'Tipo 3'),
    )

    produto_01 = models.CharField(max_length=25)
    produto_02 = models.CharField(max_length=25)
    produto_03 = models.CharField(max_length=25)
    tipo = models.CharField(max_length=5, choices=TIPOS_CHOICES)
    imagem = models.ImageField(upload_to='produtos/%Y/%m/%d')
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_modificacao = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        _imagem = Image.open(self.imagem.path)
        _imagem.thumbnail(self.MAX_SIZE)
        _imagem.save(self.imagem.path)
        
    def __str__(self):
        return self.tipo

    