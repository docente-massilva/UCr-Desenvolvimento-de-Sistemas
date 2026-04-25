from django.contrib import admin

from .models import Adotante

@admin.register(Adotante)
class AdotanteAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "email", "telefone")
    search_fields = ("nome", "email", "telefone")
    ordering = ("nome",)
