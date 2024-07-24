from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest, HttpResponse
from django.db.models import Q
from django.core.paginator import Paginator

from website.models import Customer
from website.forms.customers import CustomerForm

def create(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('customers')
    
    return HttpResponse(render(request, 'customers/create.html', {
        'form': CustomerForm()
    }))

def update(request: HttpRequest, customer_id: int) -> HttpResponse:
    customer = get_object_or_404(Customer, pk=customer_id)

    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customers')
    
    return HttpResponse(render(request, 'customers/update.html', {
        'customer': customer,
        'form': CustomerForm(instance=customer)
    }))

def index(request: HttpRequest) -> HttpResponse:
    customers = Customer.objects.all().order_by('-id')

    paginated_customers = Paginator(customers, 10)
    page_number = request.GET.get('page')
    page_customers = paginated_customers.get_page(page_number)
    
    return HttpResponse(render(request, 'customers/index.html', {
        'customers': customers,
        'page_customers': page_customers
    }))

def show(request: HttpRequest, customer_id: int) -> HttpResponse:
    customer = get_object_or_404(Customer, pk=customer_id)
    customer_initials = customer.first_name[0] + customer.last_name[0]

    return HttpResponse(render(request, 'customers/show.html', {
        'customer': customer,
        'customer_initials': customer_initials
    }))

def delete(request: HttpRequest, customer_id: int) -> HttpResponse:
    customer = get_object_or_404(Customer, pk=customer_id)
    customer.delete()
    return redirect('customers')

def search(request: HttpRequest) -> HttpResponse:
    search = request.GET.get('search', '').strip()
    customers = Customer.objects.filter(
        Q(first_name__icontains=search) |
        Q(last_name__icontains=search) |
        Q(email__icontains=search) |
        Q(phone__icontains=search)
    )

    paginated_customers = Paginator(customers, 10)
    page_number = request.GET.get('page')
    page_customers = paginated_customers.get_page(page_number)

    return HttpResponse(render(request, 'customers/index.html', {
        'customers': customers,
        'page_customers': page_customers
    }))

