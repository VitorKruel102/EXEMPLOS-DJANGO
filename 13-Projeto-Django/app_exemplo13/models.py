from django.db import models
from PIL import Image


class ItensProdutos(models.Model):
    max_size = (800, 800)
    CHOICE_TIPOS = (
        ('I1', 'Inter'),
        ('I2', 'Inter 2'),
        ('I3', 'Inter 3'),
    )

    item1 = models.CharField(max_length=25)
    tipo = models.CharField(max_length=2, choices=CHOICE_TIPOS)
    imagem = models.ImageField(upload_to='Produtos/%Y/%m/%d', null=True, blank=True)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.imagem:
            _imagem = Image.open(self.imagem.path)
            _imagem.thumbnail(self.max_size)
            _imagem.save(self.imagem.path)

    def __str__(self):
        return self.item1
