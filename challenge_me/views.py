from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def index(request):
    # name = request.POST.get("username")
    # email = request.POST.get("email")
    # password = request.POST.get("password")
    # confirm_password = request.POST.get("confirm_password")
    # if request.method == "POST":
    #     if not User.objects.filter(username=name).exists():
    #         if not User.objects.filter(email=email).exists():
    #             if password == confirm_password:
    #                 if len(password) >= 8 and len(confirm_password) >= 8:
    #                     User.objects.create_user(
    #                         username=name,
    #                         email=email,
    #                         password=password
    #                     )
    #                     messages.success(
    #                         request, "register has been successfully")
    #                     return redirect("/#subscription")

    #                 else:
    #                     messages.error(
    #                         request, "password must be Greater than 8 letters ")
    #                     print("password is exist")
    #                     return redirect("/#subscription")
    #             else:
    #                 messages.error(
    #                     request, "password is not the same confirm password")
    #                 print("password is exist")
    #                 return redirect("/#subscription")

    #         else:
    #             messages.error(
    #                 request, "email is exist")
    #             print("email is exist")
    #             return redirect("/#subscription")

    #     elif authenticate(request, username=name, password=password):
    #         print(authenticate(request, username=name, password=password))

    #         login(request, authenticate(
    #             request, username=name, password=password))
    #         return redirect(index)
    #     else:

    #         messages.error(
    #             request, "username is exist")
    #         print("username is exist")
    #         return redirect("/#subscription")

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
                            request, "register has been successfully")
                        return redirect("/#subscription")

                    else:
                        messages.error(
                            request, "password must be Greater than 8 letters ")
                        print("password is exist")
                        return redirect("/#subscription")
                else:
                    messages.error(
                        request, "password is not the same confirm password")
                    print("password is exist")
                    return redirect("/#subscription")

            else:
                messages.error(
                    request, "email is exist")
                print("email is exist")
                return redirect("/#subscription")
        else:

            messages.error(
                request, "username is exist")
            print("username is exist")
            return redirect("/#subscription")

    return redirect("/")


def login_view(request):
    name = request.POST.get("username")
    password = request.POST.get("password")

    if authenticate(request, username=name, password=password):
        print(authenticate(request, username=name, password=password))

        login(request, authenticate(
            request, username=name, password=password))
    else:
        messages.error(
            request, "username or password is wrong")
        return redirect("/#subscription")

    return redirect(index)


def logout_view(request):
    logout(request)
    return redirect("/")


def tournaments(request, slug):
    if not request.user.is_authenticated:
        return redirect("/#subscription")

    print()
    context = {
        "game": AddGame.objects.get(name=slug.replace("-", " ")),

        "tournaments": Tournament.objects.filter(game__name=slug.replace("-", " ")),
    }
    return render(request, "tournaments.html", context)


def tournament_participants(request, slug):

    # print(name)

    if not request.user.is_authenticated:
        return redirect("/#subscription")

    if request.method == "POST":
        # pass
        Player.objects.create(
            name=request.user, tournament_id=Tournament.objects.get(name=slug.replace("-", " ")).id)
    context = {
        "players": Player.objects.all(),

        "tournament": Tournament.objects.get(name=slug.replace("-", " ")),
    }
    return render(request, "tournament_participants.html", context)
