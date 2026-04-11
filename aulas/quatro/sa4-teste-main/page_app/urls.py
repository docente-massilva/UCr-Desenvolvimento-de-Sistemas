from django.urls import path
from page_app.views import index, contato, servico

urlpatterns = [
    # Cadastrar URLs aqui
    path("", index, name="page-app-index"),
    path("contato/", contato, name="page-app-contato"),
    path("servico/", servico, name="page-app-servico"),
]
