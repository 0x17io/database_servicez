from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.index, name="home"),
    path("login/", views.login, name="login"),
    path("services/", views.services.as_view(), name="services")
]