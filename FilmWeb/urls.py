from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("films.urls")),
    path("user/", include("user_auth.urls")),
    path("admin/", admin.site.urls),
]
