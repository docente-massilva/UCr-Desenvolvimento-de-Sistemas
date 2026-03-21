import random

from django.shortcuts import render


def home(request):
    context = {
        "nome": random.choice(
            [
                "Ana",
                "Carlos",
                "João",
                "Maria",
                "Marcos",
                "Sofia",
                "Pedro",
                "Luana",
                "Rafael",
            ]
        )
    }
    return render(request, "index.html", context)
