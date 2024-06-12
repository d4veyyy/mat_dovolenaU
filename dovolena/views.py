from django.shortcuts import render
from .models import Dovolena, Rezervace


def index(request):
    Dovolena = 'all inclusive'
    context = {
        'nadpis': Dovolena,
        'rezervace': Rezervace.objects.filter(dovolena__destinace=Dovolena).order_by('rok_vydani'),
        'dovolena': Dovolena.objects.all()
    }
    return render(request, 'index.html', context=context)
