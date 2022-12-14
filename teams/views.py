from django.shortcuts import render, redirect

from .models import *
from .forms import TeamForm, PlayerForm
from .decorators import *


# Create your views here.


def players(request):
    players = Player.objects.all()
    return render(request, 'players.html', {'players': players})


def teams(request):
    teams = Team.objects.all()
    return render(request, 'teams.html', {'teams': teams})


@unauthenticated_user
@allowed_users(allowed_groups=['Admin', 'Player'])
def playerInfo(request, player_id):
    player = Player.objects.get(id=player_id)
    return render(request, 'playerinfo.html', {'player': player})


def teamInfo(request, team_id):
    team_players_id = Player.objects.filter(team_id=team_id)
    players = Player.objects.filter(pk__in=team_players_id)
    return render(request, 'players.html', {'players': players})


@unauthenticated_user
@allowed_users(allowed_groups=['Admin'])
def createTeam(request):
    if request.method == "POST":
        form = TeamForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('teams')
            except:
                pass
    else:
        form = TeamForm()
    return render(request, 'createteam.html', {'form': form})


@unauthenticated_user
@allowed_users(allowed_groups=['Admin'])
def updateTeam(request, team_id):
    team = Team.objects.get(id=team_id)
    form = TeamForm(instance=team)
    if request.method == "POST":
        form = TeamForm(request.POST, request.FILES, instance=team)
        if form.is_valid():
            try:
                form.save()
                return redirect('teams')
            except:
                pass
    return render(request, 'createteam.html', {'form': form})


@unauthenticated_user
@allowed_users(allowed_groups=['Admin'])
def createPlayer(request):
    if request.method == "POST":
        form = PlayerForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('players')
            except:
                pass
    else:
        form = PlayerForm()
    return render(request, 'createplayer.html', {'form': form})


@unauthenticated_user
@allowed_users(allowed_groups=['Admin'])
def updatePlayer(request, player_id):
    player = Player.objects.get(id=player_id)
    form = PlayerForm(instance=player)
    if request.method == "POST":
        form = PlayerForm(request.POST, request.FILES, instance=player)
        if form.is_valid():
            try:
                form.save()
                return redirect('players')
            except:
                pass
    return render(request, 'createplayer.html', {'form': form})
