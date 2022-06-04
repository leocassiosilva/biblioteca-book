from django.contrib import admin
# Register your models here.
from .models import Books

class ListandoBook(admin.ModelAdmin):
    list_display = ('id', 'nome', 'autor','descricao', 'data_cadastro')
    list_display_links = ('id', 'nome')
    search_fields = ('nome','autor',)
    list_per_page = 2

admin.site.register(Books, ListandoBook)