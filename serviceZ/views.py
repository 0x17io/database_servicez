from django.shortcuts import render
from django.http import HttpResponse

from .models import Account


# Create your views here.
def index(response):
    test = Account.objects.all()
    return render(response, "homePage.html", {'contents': test})
    #return render(response,template_name="homePage.html")


