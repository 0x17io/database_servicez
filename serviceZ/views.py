from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import Account, Service, Contractor


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
