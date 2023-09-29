from django.db import models


class AddGame(models.Model):
    name = models.CharField(max_length=15)
    photo_game = models.ImageField(null=True, blank=True)
    logo_game = models.ImageField(null=True, blank=True)

    def __str__(self):

        return self.name


class Tournament (models.Model):

    name = models.CharField(max_length=15,)
    photo_game = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class About(models.Model):
    title_about = models.CharField(max_length=40)
    details_about = models.TextField(max_length=200)

    def __str__(self):
        return self.title_about


class Form(models.Model):
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "sign in"
        db_table = "app_sign in"
