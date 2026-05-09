from django.shortcuts import render, redirect, get_object_or_404

from .models import Adotante
from .forms import AdotanteForm

# Create your views here.
def index (request):
    return render(request,"page_app/partial/home.html")

def contato (request):
    return render(request, "page_app/partial/contato.html")

def servico (request):
    return render(request, "page_app/partial/services.html")

# LISTAR
def listar_adotantes(request):
    adotantes = Adotante.objects.all()
    contexto = {
        "lista_adotantes": adotantes
    }
    return render(
        request,
        "page_app/adotante/listar.html",
        contexto,
    )

# CADASTRAR
def cadastrar_adotante(request):

    if request.method == "POST":
        form = AdotanteForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("listar_adotantes")

    else:
        form = AdotanteForm()

    contexto = {
        "form": form
    }

    return render(request, "page_app/adotante/form.html", contexto)

# EDITAR
def editar_adotante(request, id):
    adotante = get_object_or_404(Adotante, pk=id)

    if request.method == "POST":
        form = AdotanteForm(request.POST, instance=adotante)

        if form.is_valid():
            form.save()
            return redirect("listar_adotantes")

    else:
        form = AdotanteForm(instance=adotante)

    contexto = {
        "form": form
    }
    return render(request, "page_app/adotante/form.html", contexto)

# EXCLUIR
def excluir_adotante(request, id):
    adotante = get_object_or_404(Adotante, pk=id)

    if request.method == "POST":
        adotante.delete()
        return redirect("listar_adotantes")
    
    contexto = {
        "adotante": adotante
    }
    return render(request, "page_app/adotante/deletar.html", contexto)

# DETALHAR
def detalhar_adotante(request, id):
    adotante = get_object_or_404(Adotante, pk=id)

    contexto = {
        "adotante": adotante
    }
    return render(request, "page_app/adotante/detalhar.html", contexto)
