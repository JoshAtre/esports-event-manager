from django.shortcuts import render, redirect

from .models import *
from .forms import CreateTeamForm


# Create your views here.
def players(request):
    players = Player.objects.all()
    return render(request, 'players.html', {'players': players})


def teams(request):
    teams = Team.objects.all()
    return render(request, 'teams.html', {'teams': teams})


def playerInfo(request, player_id):
    player = Player.objects.get(id=player_id)
    return render(request, 'playerinfo.html', {'player': player})


def createTeam(request):
    if request.method == "POST":
        form = CreateTeamForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('teams')
            except:
                pass
    else:
        form = CreateTeamForm()
    return render(request, 'createteam.html', {'form': form})


