from django.db import models


class AddGame(models.Model):
    name = models.CharField(max_length=100)
    photo_game = models.ImageField(
        null=True, blank=True, upload_to="challenge")
    logo_game = models.ImageField(null=True, blank=True, upload_to="challenge")

    def __str__(self):

        return self.name


class Tournament (models.Model):

    name = models.CharField(max_length=100)
    photo_game = models.ImageField(
        null=True, blank=True, upload_to="challenge")
    game = models.ForeignKey(
        AddGame, on_delete=models.DO_NOTHING, null=True, db_column="game")
    description = models.TextField(null=1)
    prizes = models.TextField(null=1)
    notes = models.TextField(null=1)

    def __str__(self):
        return self.name


class Player (models.Model):

    name = models.CharField(max_length=100)
    tournament = models.ForeignKey(
        Tournament, related_name="tournament", on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.name


class About(models.Model):
    title_about = models.CharField(max_length=40)
    details_about = models.TextField(max_length=200)

    def __str__(self):
        return self.title_about
