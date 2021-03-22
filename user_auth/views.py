import topmic
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render


def log_in(request):
    message = None
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method == "POST":
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect("/")
            else:
                message = "Zła nazwa użytkownika lub hasło"

        return render(
            request,
            "user_auth/login.html",
            {
                "message": message,
            },
        )


def log_out(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("/")
    else:
        return redirect("/")
