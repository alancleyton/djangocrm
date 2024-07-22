from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.models import User as UserModel

from website.models import Customer as CustomerModel
from website.models import Company as CompanyModel
from website.forms import customers as customers_forms

def create(request: HttpRequest) -> HttpResponse:
    all_users =  UserModel.objects.values()
    all_companies = CompanyModel.objects.values()

    if request.method == 'POST':
        customer_form = customers_forms.CreateForm(request.POST, all_users=all_users, all_companies=all_companies)
    else:
        customer_form = customers_forms.CreateForm(all_users=all_users, all_companies=all_companies)
    
    context = { 'form': customer_form }
    return HttpResponse(render(request, 'customers/create.html', context))

def index(request: HttpRequest) -> HttpResponse:
    customers = CustomerModel.objects.all().order_by('-id')

    paginated_customers = Paginator(customers, 10)
    page_number = request.GET.get('page')
    page_customers = paginated_customers.get_page(page_number)
    
    context = { 'customers': customers, 'page_customers': page_customers }
    return HttpResponse(render(request, 'customers/index.html', context))

def show(request: HttpRequest, customer_id: int) -> HttpResponse:
    customer = get_object_or_404(CustomerModel, pk=customer_id)
    customer_initials = customer.first_name[0] + customer.last_name[0]
    context = { 'customer': customer, 'customer_initials': customer_initials }
    return HttpResponse(render(request, 'customers/show.html', context))

def search(request: HttpRequest) -> HttpResponse:
    search = request.GET.get('search', '').strip()
    customers = CustomerModel.objects.filter(
        Q(first_name__icontains=search) |
        Q(last_name__icontains=search) |
        Q(email__icontains=search) |
        Q(phone__icontains=search)
    )

    paginated_customers = Paginator(customers, 10)
    page_number = request.GET.get('page')
    page_customers = paginated_customers.get_page(page_number)

    context = { 'customers': customers, 'page_customers': page_customers }
    return HttpResponse(render(request, 'customers/index.html', context))

