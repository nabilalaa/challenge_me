from django.db import models


class AddGame(models.Model):
    name = models.CharField(max_length=100, unique=True)
    photo_game = models.ImageField(
        null=True, blank=True, upload_to="challenge", default="https://placehold.co/600x400")
    logo_game = models.ImageField(
        null=True, blank=True, upload_to="challenge", default="https://placehold.co/600x400")

    def __str__(self):

        return self.name


GAMES = []


# for g in AddGame.objects.all():
#     GAMES.append((g.name, g.name))

# GAMES = tuple(GAMES)

# print(GAMES)


class Tournament (models.Model):

    name = models.CharField(max_length=100, unique=True)
    photo_game = models.ImageField(
        null=True, blank=True, upload_to="challenge", default="https://placehold.co/600x400")
    game = models.ForeignKey(

        AddGame, on_delete=models.SET_NULL)
    # games = models.CharField(choices=GAMES, null=True)

    description = models.TextField(null=1)
    prizes = models.TextField(null=1)
    notes = models.TextField(null=1)

    def __str__(self):
        return self.name


class Player (models.Model):

    name = models.CharField(max_length=100)
    tournament = models.ForeignKey(
        Tournament, related_name="tournament", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class About(models.Model):
    title_about = models.CharField(max_length=40)
    details_about = models.TextField(max_length=200)

    def __str__(self):
        return self.title_about
