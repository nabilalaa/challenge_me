from django.shortcuts import render, redirect
from .models import AddGame, About, Tournament
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def index(request):
    name = request.POST.get("username")
    email = request.POST.get("email")
    password = request.POST.get("password")
    confirm_password = request.POST.get("confirm_password")
    if request.method == "POST":
        # print(request.POST)
        # print(not User.objects.filter(username=name).exists(), not User.objects.filter(email=email).exists(),password == confirm_password)

        if not User.objects.filter(username=name).exists():
            print("username is exist")
            if not User.objects.filter(email=email).exists():
                print("email is exist")
                if password == confirm_password and len(password) >= 8 and len(confirm_password) >= 8:
                    print("somthing wrong in password")
                    User.objects.create_user(
                        username=name,
                        email=email,
                        password=password
                    )

        elif authenticate(request, username=name, password=password):
            print(authenticate(request, username=name, password=password))

            login(request, authenticate(
                request, username=name, password=password))
            return redirect(index)

        # Form.objects.create(
        #     # global name,
        #     name=name,
        #     email=email,
        #     password=password,
        # )
    context = {
        "add_game": AddGame.objects.all(),
        "add_about": About.objects.all(),
    }

    return render(request, "index.html", context)


def logout_view(request):
    logout(request)
    return redirect("/")


def tournament(request, slug):
    if not request.user.is_authenticated:
        return redirect("/#subscription")

    context = {
        "game": AddGame.objects.get(name=slug),

        "tournaments": Tournament.objects.filter(name=slug),
    }
    return render(request, "tournaments.html", context)
