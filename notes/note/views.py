from django.shortcuts import render
from .models import *
# Create your views here.
def homepage(request):
    notes = Note.objects.all()

    return render(request, 'home.html', context={"notes": notes})