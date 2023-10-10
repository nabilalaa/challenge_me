from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="home"),

    # authentication
    path('sign_in', sign_in, name='sign_in'),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),

    path('tournaments/<str:slug>', tournaments, name="tournaments"),
    path('tournament_participants/<str:slug>',
         tournament_participants, name="tournament_participants"),

    path('unjoind', unjoind, name='unjoind'),



]
