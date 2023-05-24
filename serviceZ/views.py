from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.shortcuts import  render, redirect
from django.contrib import messages
from .models import Account, Service, Contractor, Request, Review, Order, Client, ServiceType
from .forms import RegisterForm, UpdateAccountForm, AddServiceForm, BecomeContractorForm, BecomeClientForm, SearchBarForm, WriteReviewForm, SubmitRequestForm
from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView, ListView
import datetime

# Create your views here.
def index(response):
    """
    Landing/Search Page
    :param response:
    :return:
    """
    if response.method == "POST":
        form = SearchBarForm(response.POST)

        if form.is_valid():

            type = ServiceType.objects.filter(service__in=Service.objects
                                              .filter(Description__contains=response.POST['searchBar'])
                                              .values('TypeID')).values_list('service')


            contractors = Contractor.objects.filter(ServiceID__in=Service.objects.
                                                    filter(Description__contains=response.POST['searchBar']))\
                .values_list('MainID', 'ServiceID_id')

            print(contractors)
            contractors = [[Account.objects.get(id=x[0]).username, Service.objects.get(id=x[1]).TypeID.Type,
                            Service.objects.get(id=x[1]).Description, Service.objects.get(id=x[1]).Rate] for x in contractors]
            print(contractors)

            content = {}
            for item in contractors:
                if item[1] not in content.keys():
                    print(item[0])
                    content[item[1]] = {
                        'contractors': [item[0]],
                        'rate': item[3],
                        'descr': item[2]
                    }
                else:
                    if item[0] not in content[item[1]]['contractors']:
                        content[item[1]]['contractors'].append(item[0])

            return render(response, "search_results.html", {'content': content})
        else:
            print('Form is not valid')
            context = {'form': form}
            render(response, "home_base.html", {'form': form})
    else:
        form = SearchBarForm

    return render(response, "home_base.html", {'form': form})

class services(generic.ListView):
    form = RegisterForm()

    template_name = "services_base.html"
    context_object_name = "all_contractors"

    def get_queryset(self):
        return Contractor.objects.order_by("id")

def contractor(response, contractor_id):
    """
    Contractor views
    :param response:
    :param contractor_id:
    :return:
    """

    current_user = response.user

    contractor = Contractor.objects.filter(id=contractor_id)

    form = WriteReviewForm(response.POST)


    reviews = Review.objects.all().filter(ContractorID=contractor_id)
    if response.method == 'POST':

        main_id = Account.objects.get(username=current_user).id

        Review.objects.create(ClientID=Client.objects.filter(MainID_id=main_id).first(),
                               ContractorID=Contractor.objects.filter(id=contractor_id).first(),
                               Rating=response.POST['rating'],
                               Comment=response.POST['actual_review'])

        return render(response, "contractor_base.html", {'contractor':contractor[0], 'reviews': reviews, 'form': form})
    return render(response, "contractor_base.html", {'contractor': contractor[0], 'reviews': reviews, 'form': form})


def review(response):
    """
    List reviews.
    :param response:
    :return:
    """
    test = Account.objects.all()
    return render(response, "review_base.html", {'contents': test})

def add_review(client_id, contractor_id):
    """
    Add review, based on request.id, client, and contractor
    :param request:
    :param client_id:
    :param contractor_id:
    :return:
    """
    rating = request.POST['rate']
    text = request.POST['review_text']
    review_id = Review.objects.all()[-1].ReviewID + 1
    review = Review(ReviewID=review_id, ClientID=client_id, ContractorID=contractor_id, Rating=rating, Comment=text)
    review.save()



def register(request):
    """
    Register an account.
    :param request:
    :return:
    """
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
    """
    Submit a request
    :param response:
    :return:
    """
    #if client side list all requests client made
    client_id=1
    contractor_id=-1
    client_status = True
    #contractor_status = True
    current_user = Account.objects.filter(username=response.user)
    if current_user:
        if client_status:
            client_id = Client.objects.filter(MainID=current_user[0].pk)[0]
        else:
            contractor_id = Contractor.objects.filter(MainID=current_user[0].pk)[0]

    if client_status:
        requests = Request.objects.filter(ClientID=client_id)

        print("The requests for client id",client_id,'are',requests)

        return render(response, "request_base.html", {'requests': requests})
    #if contractor side list all requests from all clients
    else:        
        requests = Request.objects.all()
        print("Requests for contractor id",client_id," : ",requests)
        return render(response, "request_contractor_base.html", {'requests': requests})        

def delete_request(response, request_id):
    """
    Delete request.
    :param response:
    :param request_id:
    :return:
    """
    Request.objects.get(pk=request_id).delete()
    return redirect("request")       

def make_request(response, service_id):
    """
    Make a request.
    :param response:
    :param service_id:
    :return:
    """
    # current_user = Account.objects.get(username=response.user)
    # client_id = Client.objects.filter(MainID=current_user[0].pk)
    current_username = Account.objects.filter(username=response.user)
    print(current_username)
    client_id = Client.objects.filter(MainID=current_username[0].pk)[0]
    print(client_id)
    service_id = Service.objects.filter(id=service_id)[0]
    r = Request(ClientID=client_id, ServiceID=service_id, Timestamp = datetime.datetime.now())
    r.save()
    return redirect("services")

def order(response):
    """
    Observe current orders.
    :param response:
    :return:
    """
    #if client side list all orders client made
    client_id=1
    contractor_id=-1
    client_status = True
    current_user = Account.objects.filter(username=response.user)
    if current_user:
        if client_status:
            client_id = Client.objects.filter(MainID=current_user[0].pk)[0]
        else:
            contractor_id = Contractor.objects.filter(MainID=current_user[0].pk)[0]

    #contractor_status = True
    if client_status:
        orders = Order.objects.filter(ClientID=client_id)
        
        print("The orders for client id",client_id,'are',orders)

        return render(response, "order_base.html", {'orders': orders})
    #if contractor side list all orders from all clients
    else:        
        orders = Order.objects.filter(ContractorID=contractor_id)
        print(orders)
        return render(response, "order_contractor_base.html", {'orders': orders})        

def delete_order(response, order_id):
    """
    Delete order
    :param response:
    :param order_id:
    :return:
    """
    Order.objects.get(pk=order_id).delete()
    return redirect("order")

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
    Getting reviews for just the logged in user. Assume you only have 1 client ID per user. This is just to showcase
    functionality.
    :param request:
    :return:
    """
    current_username = Account.objects.get(username=request.user).id

    client_id = Client.objects.filter(MainID=current_username).values()[0]['id']
    account_data = Account.objects.get(username=request.user)

    all_reviews = Review.objects.filter(ClientID = client_id) #Review.objects.filter(ClientID = client_id)
    return render(request, "accountPage.html", {'contents': all_reviews, 'current_user': account_data})

def load_account(request):
    """
    Loads account, additionally allows you to updated the zipcode/language of the user.
    :param request:
    :return: Account Page
    """

    current_user_data = Account.objects.get(username=request.user)
    client_main_ids = Client.objects.all().values_list('MainID', flat=True)
    conntractor_main_ids = Contractor.objects.all().values_list('MainID', flat=True)


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
        return render(request, "accountPage.html", {'content': current_user_data, 'form': form,
                                                    'clientInfo': client_main_ids, 'contractorInfo': conntractor_main_ids})

    return render(request, "accountPage.html", {'content': current_user_data, 'form': form,
                                                'clientInfo': client_main_ids, 'contractorInfo': conntractor_main_ids})
def addService (request):
    """
    Add a service that a client is interested in.
    :param request:
    :return:
    """
    current_user_data = Account.objects.get(username=request.user)

    if request.method == "POST":
        form = AddServiceForm(request.POST)

        if form.is_valid():

            ServiceType.objects.create(Type=request.POST['ServiceType'])

            return redirect('account_page')
        else:
            print('Form is not valid')
            print(form.__dict__)
            messages.error(request, 'Error Processing Your Request')
            context = {'form': form}
            return render(request, 'addServiceType.html', context)
    else:
        form = AddServiceForm

    #
    return render(request, "addServiceType.html", {'content': current_user_data, 'form': form})

def become_client(request):
    """
    Confirm that you would like to become a client.
    :param request:
    :return:
    """
    current_user_data = Account.objects.get(username=request.user)

    if request.method == "POST":
        form = BecomeClientForm(request.POST)

        if form.is_valid():

            Client.objects.create(MainID=request.user)
            print("made it?")

            return redirect('account_page')
        else:
            print('Form is not valid')
            context = {'form': form}
            return render(request, 'become_client.html', context)
    else:
        form = BecomeClientForm

    return render(request, "become_client.html", {'content': current_user_data, 'form': form})


def become_contractor(request):
    """
    Become a contractor!
    :param request:
    :return:
    """
    current_user_data = Account.objects.get(username=request.user)

    if request.method == "POST":
        form = BecomeContractorForm(request.POST)

        if form.is_valid():

            print()
            Test = Service.objects.create(TypeID=ServiceType.objects.get(id=request.POST['service_type_id']),
                                   Description=request.POST['description'],
                                   Rate=request.POST['rate'])

            Contractor.objects.create(MainID=current_user_data, ServiceID=Service.objects.get(id=Test.id),
                                        Availability=True)


            return redirect('account_page')
        else:
            print('Form is not valid')
            context = {'form': form}
            return render(request, 'become_contractor.html', context)
    else:
        form = BecomeContractorForm

    return render(request, "become_contractor.html", {'content': current_user_data, 'form': form})

def typeID_to_name(num):
    """
    Helper function, extract servicetype name.
    :param num:
    :return:
    """
    serv_helper = ServiceType.objects.filter(id=num).values_list('Type', flat=True)
    serv_helper = serv_helper.first().Type
    return serv_helper
