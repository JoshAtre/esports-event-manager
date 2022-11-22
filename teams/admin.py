from django.contrib import admin
from .models import Team
from .models import Player

# Register your models here.
admin.site.register(Team)
admin.site.register(Player)
