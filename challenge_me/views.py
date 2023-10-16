from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    context = {
        "add_game": AddGame.objects.all(),
        "add_about": About.objects.all(),
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


def tournaments(request, slug):
    if not request.user.is_authenticated:
        return redirect("/#subscription")

    context = {
        "game": AddGame.objects.get(name=slug.replace("-", " ")),

        "tournaments": Tournament.objects.filter(game__name=slug.replace("-", " ")),
    }
    return render(request, "tournaments.html", context)


def tournament_participants(request, slug):
    print(request.GET)
    players_list = Player.objects.all()
    paginator = Paginator(players_list, 3)
    page_number = request.GET.get("page", 1)
    try:

        players = paginator.page(page_number)

    except EmptyPage:
        players = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        players = paginator.page(1)

        pass
    if Player.objects.filter(name=request.user):
        messsage_joind = "leave"
    else:
        messsage_joind = "join"

    if not request.user.is_authenticated:
        return redirect("/#subscription")

    if request.method == "POST":
        if (not Player.objects.filter(name=request.user)):
            Player.objects.create(
                name=request.user, tournament_id=Tournament.objects.get(name=slug.replace("-", " ")).id)
            messsage_joind = "leave"
        else:

            Player.objects.filter(name=request.user).delete()
            messsage_joind = "join"

    context = {
        "players": players,
        "message": messsage_joind,
        "tournament": Tournament.objects.get(name=slug.replace("-", " ")),
    }
    return render(request, "tournament_participants.html", context)


def unjoind(request):
    print(request)
