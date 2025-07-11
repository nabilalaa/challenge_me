from django.shortcuts import render, redirect,HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    context = {
        "games": Game.objects.all(),
        "about": About.objects.all(),
    }

    return render(request, "index.html", context)


def sign_in(request):
    name = request.POST.get("username")
    email = request.POST.get("email")
    password = request.POST.get("password")
    confirm_password = request.POST.get("confirm_password")
    if request.method == "POST":
        if not User.objects.filter(username=name).exists():
            if not User.objects.filter(email=email).exists():
                if password == confirm_password:
                    if len(password) >= 8 and len(confirm_password) >= 8:
                        User.objects.create_user(
                            username=name,
                            email=email,
                            password=password
                        )
                        messages.success(
                            request, "register has been successfully", extra_tags="sign_in")
                        return redirect("/#subscription")

                    else:
                        messages.error(
                            request, "password must be Greater than 8 letters ", extra_tags="sign_in")
                        print("password is exist")
                        return redirect("/#subscription")
                else:
                    messages.error(
                        request, "password is not the same confirm password", extra_tags="sign_in")
                    print("password is exist")
                    return redirect("/#subscription")

            else:
                messages.error(
                    request, "email is exist", extra_tags="sign_in")
                print("email is exist")
                return redirect("/#subscription")
        else:

            messages.error(
                request, "username is exist", extra_tags="sign_in")
            print("username is exist")
            return redirect("/#subscription")

    return redirect(index)


def login_view(request):
    name = request.POST.get("username")
    password = request.POST.get("password")

    if authenticate(request, username=name, password=password):
        print(authenticate(request, username=name, password=password))

        login(request, authenticate(
            request, username=name, password=password))
    else:
        messages.error(
            request, "username or password is wrong", extra_tags="login")
        return redirect("/#subscription")

    return redirect(index)


def logout_view(request):
    logout(request)
    return redirect(index)



def game_list(request):
    context = {
        "games": Game.objects.all()
    }
    return render(request, 'game_list.html', context)    

def tournaments_by_game(request, slug):
    if not request.user.is_authenticated:
        return redirect("/#subscription")

    context = {
        "game": Game.objects.get(name=slug.replace("-", " ")),

        "tournaments": Tournament.objects.filter(game__name=slug.replace("-", " "),is_active=True),
    }
    return render(request, "tournament_list_by_game.html", context)


def tournament_details(request, slug):
    if not request.user.is_authenticated:
        return redirect("/#subscription")

    players = Player.objects.filter(tournament_id=Tournament.objects.get(title=slug.replace("-", " ")).id)
    max_participants = Tournament.objects.get(title=slug.replace("-", " ")).max_participants

    if  Player.objects.filter(name=request.user.username):
        messsage_joind = "leave"
    else:

        messsage_joind = "join"

    if players.count() == max_participants and not Player.objects.filter(name=request.user.username):
        messsage_joind = "max participants" 

    context = {
        "players": Player.objects.filter(tournament_id=Tournament.objects.get(title=slug.replace("-", " ")).id),
        "playersList": players.values_list("name",flat=True),
        "message": messsage_joind,
        "tournament": Tournament.objects.get(title=slug.replace("-", " ")),
    }
    return render(request, "tournament_details.html", context)


def join(request,slug):
    players = Player.objects.filter(tournament_id=Tournament.objects.get(title=slug.replace("-", " ")).id)
    max_participants = Tournament.objects.get(title=slug.replace("-", " ")).max_participants
    if not Player.objects.filter(name=request.user.username) :
        
        Player.objects.create(name=request.user.username,tournament_id=Tournament.objects.get(title=slug.replace("-", " ")).id)
        messsage_joind = "leave"

        
    else:
        Player.objects.filter(name=request.user).delete()

        messsage_joind = "join"

    if players.count() == max_participants and not Player.objects.filter(name=request.user.username):
        messsage_joind = "max participants" 

        
    context = {
        "players": Player.objects.filter(tournament_id=Tournament.objects.get(title=slug.replace("-", " ")).id),
        "playersList": players.values_list("name",flat=True),
        "message": messsage_joind,

        "tournament": Tournament.objects.get(title=slug.replace("-", " ")),
    }
    return render(request, "components/players.html", context)
