from django.urls import path

from user_auth.views import LogIn, log_out

urlpatterns = [
    path("login/", LogIn.as_view(), name="login"),
    path("logout/", log_out, name="logout"),
]
