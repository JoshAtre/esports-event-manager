"""esports-event-manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from events import views as eventsViews
from teams import views as teamsViews
from accounts import views as accountsViews
from calendarApp import views as calendarViews
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', accountsViews.home, name='home'),
    path('players/', teamsViews.players, name='players'),
    path('players/create_player/', teamsViews.createPlayer, name='createPlayer'),
    path('players/update_player/<str:player_id>', teamsViews.updatePlayer, name='updatePlayer'),
    path('players/<str:player_id>/', teamsViews.playerInfo, name='playerInfo'),
    path('teams/create_team', teamsViews.createTeam, name='createTeam'),
    path('teams/update_team/<str:team_id>', teamsViews.updateTeam, name='updateTeam'),
    path('teams/<str:team_id>', teamsViews.teamInfo, name='teamInfo'),
    path('calendar/', calendarViews.calendar, name='calendar'),
    # path('events/', include('events.urls')),
    path('events/', eventsViews.events, name='events'),
    # path('events/<int:event_id>', eventsViews.detail, name='eventDetail'),
    path('events/detail/<int:event_id>', eventsViews.detail, name='eventDetail'),
    path('accounts/', include('accounts.urls')),
    path('teams/', teamsViews.teams, name='teams'),
    path('calendar/', include('calendarApp.urls')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)