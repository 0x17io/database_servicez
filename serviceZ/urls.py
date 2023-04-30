from django.urls import path
from . import views

urlpatterns = [
    #path("", views.index, name="index"),
    path("", views.index, name="home"),
    path("login/", views.login, name="login"),
    path("services/", views.services.as_view(), name="services"),
    path("<int:pk>/contractor/", views.contractor.as_view(), name="contractor"),
    path("register", views.register, name="register"),
    path("request/", views.request, name="request")
]