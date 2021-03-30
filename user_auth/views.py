from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render, reverse
from django.views import View

from .forms import UserLoginForm


class LogIn(View):
    def get(self, request):
        message = request.GET.get("message", None)
        form = UserLoginForm()
        context = {
            "message": message,
            "form": form,
        }
        if request.user.is_authenticated:
            return redirect("/")
        else:
            return render(request, "user_auth/login.html", context)

    def post(self, request):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=email, password=password)
            if user:
                login(request, user)
                return redirect("/")
            else:
                return redirect(
                    reverse("login") + "?message=Zła nazwa użytkonika lub hasło"
                )


def log_out(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("/")
    else:
        return redirect("/")
