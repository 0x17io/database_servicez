from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(response):
    return render(response,template_name="homePage.html")#HttpResponse("Welcome to ServiceZ")

def login(response):
    return render(response,template_name="loginPage.html")#HttpResponse("Welcome to ServiceZ")