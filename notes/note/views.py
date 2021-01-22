from django.shortcuts import render
from .models import *


# Create your views here.
def homepage(request):

    return render(request, 'home.html')


def note(request):
    notes = Note.objects.all()

    return render(request, 'notes.html', context={"notes": notes})
