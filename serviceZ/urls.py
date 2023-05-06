from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("login/", views.sign_in, name="login"),
    path("services/", views.services.as_view(), name="services"),
    path("<int:contractor_id>/contractor/", views.contractor, name="contractor"),
    path("register", views.register, name="register"),
    path("request/", views.request, name="request"),
    path("order/", views.order, name="order"),
    path("review/", views.review, name="review"),
    path("<int:contractor_id>/contractor/", views.add_review, name="add_review"),
    path("accountPage/", views.load_account, name="account_page"),
]