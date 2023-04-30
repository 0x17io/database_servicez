from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.shortcuts import  render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .models import Account, Service, Contractor, Request
from .forms import RegisterForm

# Create your views here.
def index(response):
    test = Account.objects.all()
    return render(response, "home_base.html", {'contents': test})
    #return render(response,template_name="homePage.html")


def login(response):
    test = Account.objects.all()
    return render(response, "login_base.html", {'contents': test})
    #return render(response,template_name="homePage.html")

class services(generic.ListView):
    template_name = "services_base.html"
    context_object_name = "all_contractors"

    def get_queryset(self):
        return Contractor.objects.order_by("ContractorID")

    # all_services = Services
    # print(all_services)
    # return render(response, "services.html", {'contents': all_services})
    #return render(response,template_name="homePage.html")

class contractor(generic.DetailView):
    model = Contractor
    template_name = "contractor_base.html"
    context_object_name = 'contractor_info'

def register(request):
    if request.method == 'GET':
        form  = RegisterForm()
        context = {'form': form}
        return render(request, 'register_base.html', context)
    if request.method == 'POST':
        form  = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('home')
        else:
            print('Form is not valid')
            messages.error(request, 'Error Processing Your Request')
            context = {'form': form}
            return render(request, 'register_base.html', context)

    return render(request, 'register_base.html', {})

def request(response):
    test = Account.objects.all()
    return render(response, "request_base.html", {'contents': test})