from django import forms

from .models import Adotante

class AdotanteForm(forms.ModelForm):
    class Meta:
        model = Adotante
        fields = [
            "nome",
            "email",
            "telefone",
        ]
        labels = {
            "nome": "Nome Completo",
            "email": "E-mail",
            "telefone": "Telefone",
        }
