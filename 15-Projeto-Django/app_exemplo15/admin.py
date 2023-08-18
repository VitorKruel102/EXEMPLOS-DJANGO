from django.contrib import admin

from app_exemplo15.models import Produtos

@admin.register(Produtos)
class ProdutosAdmin(admin.ModelAdmin):

    list_display = ('produto_01', 'produto_02', 'produto_03', 'tipo')