from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Team(models.Model):
    color = models.CharField(max_length=50)
    game = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='teams/images/', blank=True)
    
    def __str__(self):
        return f"{self.game} {self.color}"

class Player(models.Model):
    """user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)"""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    discord = models.CharField(max_length=100)
    rank = models.CharField(max_length=100)
    rank_division = models.IntegerField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to='teams/images/')

    def __str__ (self):
        return (self.name)
