from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="home"),

    path('logout', logout_view, name='logout'),

    path('tournaments/<str:slug>', tournaments, name="tournaments"),
    path('tournament_participants/<str:slug>',
         tournament_participants, name="tournament_participants"),


]
