from django.shortcuts import redirect, render
from .models import Event
from .forms import *
from teams.models import Player
from events.models import EventRegistration
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from teams.decorators import *


# Create your views here.
def events(request):
    if request.method == "GET":
        events = Event.objects.all()
        return render(request, 'events.html', {'events': events, 'eventFilter': 'allEvents'})
    else:
        event_filter = request.POST['eventFilter']
        if event_filter == 'allEvents':
            events = Event.objects.all()
        elif event_filter == 'unregisteredEvents':
            # Show unregistered events
            player_team_id = get_team_id(request.user)
            registered_event_ids = EventRegistration.objects.filter(team_id=player_team_id).values_list('event_id', flat=True)
            events = Event.objects.exclude(pk__in=registered_event_ids)
        else:
            # Show only my team's events
            player_team_id = get_team_id(request.user)
            registered_event_ids = EventRegistration.objects.filter(team_id=player_team_id).values_list('event_id', flat=True)
            events = Event.objects.filter(pk__in=registered_event_ids)
        return render(request, 'events.html', {'events': events, 'eventFilter': event_filter})


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
        event_registration = EventRegistration(event_id=event_id, team_id=player_team_id)
        event_registration.save()

        event = get_object_or_404(Event, pk=event_id)

        # Send email to the player
        message = "You've successfully registered your team for " + event.name + "!"
        print(settings.EMAIL_HOST_USER)
        print(settings.EMAIL_HOST_PASSWORD)
        send_mail(subject="Event registration", message=message, from_email="SCU eSports <noreply@egames.scu.edu>",
                  recipient_list=[request.user.username])
        messages.success(request, "You've successfully registered your team for this event")

        return render(request, 'detail.html', {'event': event, 'registered': True})


def get_team_id(user):
    if user.is_authenticated:
        # Note that usernames must be email addresses
        email = user.username
        if email is not None:
            matching_players = Player.objects.filter(email=email)
            if len(matching_players) > 0:
                player = matching_players[0]
                return player.team_id
    
    return None

@unauthenticated_user
@allowed_users(allowed_groups=['Admin'])
def createEvent(request):
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('events')
            except:
                pass
    else:
        form = EventForm()
    return render(request, 'createevent.html', {'form': form})

@unauthenticated_user
@allowed_users(allowed_groups=['Admin'])
def updateEvent(request, event_id):
    event = Team.objects.get(id=event_id)
    form = EventForm(instance=event)
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            try:
                form.save()
                return redirect('events')
            except:
                pass
    return render(request, 'createevent.html', {'form': form})