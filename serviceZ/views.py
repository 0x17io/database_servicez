from django.shortcuts import render
from django.http import HttpResponse
from .models import account
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def index(response):
    return render(response,template_name="homePage.html")#HttpResponse("Welcome to ServiceZ")

def login(response):
    contents = account.objects.all() # get all contents from account table
    return render(response, "loginPage.html", {'contents': contents})

# Renee's part
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # do login stuff here test
            pass
    else:
        form = AuthenticationForm(request)
    return render(request, 'loginPage.html', {'form': form})
