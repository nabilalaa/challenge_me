from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="home"),

    path('logout', logout_view, name='logout'),

    path('tournament/<str:slug>', tournament, name="tournament"),

]
