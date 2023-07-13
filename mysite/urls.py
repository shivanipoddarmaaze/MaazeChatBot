from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path("chat/", include("chat.urls")),
    path("", views.home, name="home"),
    path("admin/", admin.site.urls),
]