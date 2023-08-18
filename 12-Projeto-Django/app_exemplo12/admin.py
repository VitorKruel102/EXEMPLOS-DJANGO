from django.contrib import admin
from app_exemplo12.models import ItemPagina
# Register your models here.
@admin.register(ItemPagina)
class ItemPaginaAdmin(admin.ModelAdmin):

    list_display = ('item1', 'tipo', 'imagem')