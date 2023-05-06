from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.shortcuts import  render, redirect
from django.contrib import messages
from .models import Account, Service, Contractor, Request, Review, Order, Client
from .forms import RegisterForm, UpdateAccountForm
from django.contrib.auth import authenticate, login

# Create your views here.
def index(response):
    test = Account.objects.all()
    return render(response, "home_base.html", {'contents': test})
    #return render(response,template_name="homePage.html")


def loginCus(response):
    test = Account.objects.all()
    return render(response, "accountPage.html", {'contents': test})
    #return render(response,template_name="homePage.html")

class services(generic.ListView):
    template_name = "services_base.html"
    context_object_name = "all_contractors"

    def get_queryset(self):
        return Contractor.objects.order_by("id")

    # all_services = Services
    # print(all_services)
    # return render(response, "services.html", {'contents': all_services})
    #return render(response,template_name="homePage.html")

# class contractor(generic.DetailView):
#     model = Contractor
#     template_name = "contractor_base.html"
#     context_object_name = 'contractor_info'

def contractor(response, contractor_id):
    contractor = Contractor.objects.filter(id=contractor_id)
    reviews = Review.objects.all()

    return render(response, "contractor_base.html", {'contractor':contractor[0], 'reviews': reviews})


def review(response):
    test = Account.objects.all()
    return render(response, "review_base.html", {'contents': test})

def add_review(request, client_id, contractor_id):
    if request.method == 'POST':
        rating = request.POST['rate']
        text = request.POST['review_text']
        review_id = Review.objects.all()[-1].ReviewID + 1
        review = Review(ReviewID=review_id,ClientID=client_id,ContractorID=contractor_id,Rating=rating,Comment=text)
        review.save()
        return render(request, "contractor_base.html")
    else:
        return render(request, 'contractor_base.html')


def register(request):
    if request.method == 'GET':
        form = RegisterForm()
        context = {'form': form}
        return render(request, 'register_base.html', context)
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():

            form.save()

            latestRecord = Account.objects.get(username=request.POST['username'])
            latestRecord.FirstName = request.POST['first_name']
            latestRecord.LastName = request.POST['last_name']
            latestRecord.EmailAddr = request.POST['email']
            latestRecord.save()

            user = form.cleaned_data.get('username')

            messages.success(request, 'Account was created for the following user: ' + user)
            return redirect('home')
        else:
            print('Form is not valid')
            messages.error(request, 'Error Processing Your Request')
            context = {'form': form}
            return render(request, 'register_base.html', context)

    return render(request, 'register_base.html', {})

def request(response):
    if True:
        test = Request.objects.all()
        return render(response, "request_base.html", {'contents': test})
    else:        
        test = Request.objects.all()
        return render(response, "request_contractor_base.html", {'contents': test})        

def order(response):
    if True:
        test = Order.objects.all()
        return render(response, "order_base.html", {'contents': test})

def sign_in(request):
    """
    Sign in user.
    :param request:
    :return:
    """
    user = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(user)
    if user is not None:
        if user.is_active:
            login(request, user)
            messages.success(request, ("worked!"))
        return redirect("account_page") #accountPage.html", {})
    else:
        messages.success(request,("error dudeee"))
        return render(request, "login_base.html", {})

def helper_function (request):
    """
    Getting reviews for just the logged in user. Assume you only have 1 client ID per user.
    :param request:
    :return:
    """
    current_username = Account.objects.get(username=request.user).id

    client_id = Client.objects.filter(MainID=current_username).values()[0]['id']

    account_data = Account.objects.get(username=request.user)
    #Client.objects.filter(MainID=Account.objects.get(username="super_user").id).values()[0]['id']
    all_reviews = Review.objects.filter(ClientID = client_id) #Review.objects.filter(ClientID = client_id)
    return render(request, "accountPage.html", {'contents': all_reviews, 'current_user': account_data})

def load_account(request):
    """
    Loads account, additinoally allows you to updated the zipcode/language of the user.
    :param request:
    :return: Account Page
    """

    current_user_data = Account.objects.get(username=request.user)

    if request.method == 'POST':
        form = UpdateAccountForm(request.POST)

        if form.is_valid():

            currentRecord = Account.objects.get(username=current_user_data)
            currentRecord.Zipcode = request.POST['Zipcode']
            currentRecord.Language = request.POST['Language']
            currentRecord.save()

            messages.success(request, "Updated Account")

            return redirect('account_page')

        else:
            print('Form is not valid')
            messages.error(request, 'Error Processing Your Request')
            context = {'form': form}
            return render(request, 'accountPage.html', context)

    else:
        # Pull form when initially getting to page
        form = UpdateAccountForm
        print(current_user_data.username)
        return render(request, "accountPage.html", {'content': current_user_data, 'form': form})

    return render(request, 'accountPage.html', {'content': current_user_data, 'form': form})

