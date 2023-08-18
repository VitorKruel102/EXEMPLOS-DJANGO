from django.db import models
from PIL import Image

# Create your models here.
class HomeDados(models.Model):

    item1 = models.CharField(max_length=5)
    item2 = models.CharField(max_length=10)
    item3 = models.CharField(max_length=15)
    imagem = models.ImageField(upload_to='Home/HomeDados/%Y/%m/%d', blank=True, default=None)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_modificacao = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.imagem:
            _imagem = Image.open(self.imagem.path)
            max_size = (250, 250)
            _imagem.thumbnail(max_size)
            _imagem.save(self.imagem.path)
