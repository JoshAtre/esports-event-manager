from django.db import models
from teams.models import Team

# Create your models here.


class Event(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    venues = models.CharField(max_length=200)
    image = models.ImageField(upload_to="events/images/")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.name is None or len(self.name) == 0:
            raise Exception("name must be provided")
        if self.start_date >= self.end_date:
            raise Exception("end_date must be after start_date")

    def __str__(self):
        return self.name


class EventRegistration(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.team} - {self.event}"
