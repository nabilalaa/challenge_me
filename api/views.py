from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PlayersSerializers
from challenge_me.models import Player
from rest_framework.pagination import PageNumberPagination


@api_view(["GET"])
def players(request):
    count = Player.objects.all().count()
    paginator = PageNumberPagination()
    page_size = 3
    paginator.page_size = page_size

    players = paginator.paginate_queryset(Player.objects.all(), request)
    serializers = PlayersSerializers(players, many=True)

    return Response({"players": serializers.data, "page_size": page_size})


@api_view(["GET"])
def getPlayersId(request, id):
    print(id)
    player = get_object_or_404(Player, id=id)
    serializers = PlayersSerializers(player)

    return Response(serializers.data)
