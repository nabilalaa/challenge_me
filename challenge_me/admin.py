from django.contrib import admin
from .models import *

admin.site.register(Game)
admin.site.register(Tournament)
admin.site.register(Player)
admin.site.register(TournamentRegistration)

admin.site.register(About)
