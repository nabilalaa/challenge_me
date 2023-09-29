from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="home"),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('chat', chat, name="chat"),
    path('tournament/<str:slug>', tournament, name="tournament"),

]
