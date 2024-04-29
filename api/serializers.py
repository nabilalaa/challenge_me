from rest_framework import serializers
from challenge_me.models import Player


class PlayersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = "__all__"
