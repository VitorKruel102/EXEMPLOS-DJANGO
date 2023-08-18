from django.db import models

from PIL import Image

class Produtos(models.Model):
    CATEGORIAS = (
        ('Roupa M', 'Roupa Masculina'),
        ('Roupa F', 'Roupa Feminina'),
        ('Carros', 'Carros'),
        ('Motos', 'Motos'),
        ('Casa', 'Casa'),
    )
    MAX_SIZE = (250, 250)

    titulo = models.CharField(max_length=50)
    descricao = models.TextField()
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    imagem_produto = models.ImageField(upload_to='produtos/%Y/%m/%d')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        _imagem = Image.open(self.imagem_produto.path)
        _imagem.thumbnail(self.MAX_SIZE)
        _imagem.save(self.imagem_produto.path)

    class Meta:
        # Defina o nome personalizado da tabela aqui
        verbose_name_plural = 'Produto'

    def __str__(self):
        return self.titulo