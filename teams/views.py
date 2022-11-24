from django.shortcuts import render
from .models import *

# Create your views here.
def players(request):
    players = Player.objects.all()
    return render(request, 'players.html', {'players': players})

def teams(request):
    teams = Team.objects.all()
    return render(request, 'teams.html', {'teams': teams})
