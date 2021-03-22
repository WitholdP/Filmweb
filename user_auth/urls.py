import topmic
from django.urls import path

from user_auth.views import log_in, log_out

urlpatterns = [
    path("login/", log_in, name="login"),
    path("logout/", log_out, name="logout"),
]
