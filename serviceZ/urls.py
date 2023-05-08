from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("login/", views.sign_in, name="login"),
    path("services/", views.services.as_view(), name="services"),
    path("<int:contractor_id>/contractor/", views.contractor, name="contractor"),
    #path("<int:contractor_id>/contractor/", views.contractor, name="request_contractor"),
    path("register", views.register, name="register"),
    path("request/", views.request, name="request"),
    path("order/", views.order, name="order"),
    path("review/", views.review, name="review"),
    path("<int:contractor_id>/contractor/add_review", views.add_review, name="add_review"),
    path("accountPage/", views.load_account, name="account_page"),
    path("addServiceTypes/", views.addService, name="add_service_types"),
    path("becomeClient/", views.become_client, name="become_client"),
    path("becomeContractor/", views.become_contractor, name="become_contractor"),
    path("searchResults/", views.index, name="search_results"),
    path("<int:request_id>/delete_request", views.delete_request, name="delete_request"),
    path("<int:order_id>/delete_order", views.delete_order, name="delete_order"),
]