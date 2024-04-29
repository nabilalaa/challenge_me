from django.urls import path
from .views import *

urlpatterns = [
    path("players", players, name="players"),
    path("players/<int:id>", getPlayersId, name="players")


]
