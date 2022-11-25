from django.shortcuts import render, redirect

from .models import *
from .forms import TeamForm


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
        form = TeamForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('teams')
            except:
                pass
    else:
        form = TeamForm()
    return render(request, 'createteam.html', {'form': form})

def updateTeam(request, team_id):
    team = Team.objects.get(id=team_id)
    form = TeamForm(instance=team)
    if request.method == "POST":
        form = TeamForm(request.POST, instance=team)
        if form.is_valid():
            try:
                form.save()
                return redirect('teams')
            except:
                pass
    return render(request, 'createteam.html', {'form': form})


