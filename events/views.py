from django.shortcuts import redirect, render
from .models import Event
from teams.models import Player
from events.models import EventRegistration
from django.shortcuts import get_object_or_404
from django.contrib import messages


# Create your views here.
def events(request):
    events = Event.objects.all()
    return render(request, 'events.html', {'events': events})

def detail(request, event_id):
    player_team_id = get_team_id(request.user)            

    if request.method == "GET":
        # See if the player's team is already registered for the event
        regs = EventRegistration.objects.filter(event_id=event_id, team_id=player_team_id)
        registered = False
        if len(regs) > 0:
            registered = True
            
        event = get_object_or_404(Event, pk=event_id)
        return render(request, 'detail.html', {'event': event, 'registered': registered})
    else:
        # Register the player's team for the event        
        eventRegistration = EventRegistration(event_id=event_id, team_id=player_team_id)
        eventRegistration.save()
        
        messages.success(request, "You've successfully registered your team for this event")
    
        # return redirect('events') # TODO: Check
        event = get_object_or_404(Event, pk=event_id)
        return render(request, 'detail.html', {'event': event, 'registered': True})
        

def get_team_id(user):
    if user.is_authenticated:
        email = user.email
        if email is not None:
            matchingPlayers = Player.objects.filter(email=email)
            if len(matchingPlayers) > 0:
                player = matchingPlayers[0]
                return player.team_id
    
    return None
    