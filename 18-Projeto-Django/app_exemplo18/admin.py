from django.contrib import admin
from app_exemplo18.models import Produtos

# Register your models here.
@admin.register(Produtos)
class ProdutosAdmin(admin.ModelAdmin):

    list_display = ('id', 'titulo', 'categoria')