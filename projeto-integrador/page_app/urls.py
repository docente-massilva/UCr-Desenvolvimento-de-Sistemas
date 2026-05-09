from django.urls import path
from page_app.views import (
    index,
    contato,
    servico,
    listar_adotantes,
    cadastrar_adotante,
    editar_adotante,
    excluir_adotante,
    detalhar_adotante,
)

urlpatterns = [
    path("", index, name="page-app-index"),
    path("contato/", contato, name="page-app-contato"),
    path("servico/", servico, name="page-app-servico"),
    path("adotantes/", listar_adotantes, name="listar_adotantes"),
    path("adotantes/cadastrar/", cadastrar_adotante, name="cadastrar_adotante"),
    path("adotantes/<int:id>/editar/", editar_adotante, name="editar_adotante"),
    path("adotantes/<int:id>/excluir/", excluir_adotante, name="excluir_adotante"),
    path("adotantes/<int:id>/", detalhar_adotante, name="detalhar_adotante"),
]
