from django.db import models
from PIL import Image


class ItemPagina(models.Model):
    ITEM_CHOICE = (
        ('I1', 'Item 1'),
        ('I2', 'Item 2'),
        ('I3', 'Item 3'),
        ('I4', 'Item 4'),
    )

    item1 = models.CharField(max_length=12)
    tipo = models.CharField(max_length=2, choices=ITEM_CHOICE)
    imagem = models.ImageField(upload_to='Itens/%Y/%m/%d')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        _imagem = Image.open(self.imagem.path)
        max_size = (800, 800)
        _imagem.thumbnail(max_size)
        _imagem.save(self.imagem.path)