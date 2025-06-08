from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):
    name = models.CharField(max_length=100, unique=True)
    photo_game = models.ImageField(
        null=True, blank=True, upload_to="challenge")
    photo_game_url = models.URLField(null=True, blank=True,)
    logo_game = models.ImageField(
        null=True, blank=True, upload_to="challenge")
    logo_game_url = models.URLField(null=True, blank=True,)

    

    def __str__(self):

        return self.name


class Tournament(models.Model):
    title = models.CharField(max_length=100, unique=True,null=True)
    photo_game = models.ImageField(
        null=True, blank=True, upload_to="challenge")

    game = models.ForeignKey(Game, on_delete=models.SET_NULL, null=True)
    description = models.TextField(null=1)
    prizes = models.TextField(null=1)
    notes = models.TextField(null=1)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    is_active = models.BooleanField(default=True,null=1)


    def __str__(self):
        return self.title


class Player (models.Model):

    name = models.CharField(max_length=100)
    tournament = models.ForeignKey(
        Tournament, related_name="tournament", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
    
class TournamentRegistration(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name="player",related_name="player")
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    registered_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('player', 'tournament')  # لاعب واحد لكل بطولة

    def __str__(self):
        return f"{self.player.username} -> {self.tournament.title}"


class About(models.Model):
    title_about = models.CharField(max_length=40)
    details_about = models.TextField(max_length=200)

    def __str__(self):
        return self.title_about
