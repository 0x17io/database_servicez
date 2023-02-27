# Adjust this file for views.
# request -> response OR called request -> response
from django.shortcuts import render
from django.http import HttpResponse

def hello_world(response):
    return HttpResponse("whats up")
