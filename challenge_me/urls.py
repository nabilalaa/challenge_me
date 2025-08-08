from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="home"),

    # authentication
    path('sign_in', sign_in, name='sign_in'),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),


    # path('games/', game_list, name='game_list'),


    path('games/<str:slug>', tournaments_by_game, name="tournaments_by_game"),

    path('games/tournament/<str:slug>',
         tournament_details, name="tournament_details"),

    path('join/<slug:slug>', join, name='join'),



]
