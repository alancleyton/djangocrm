from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest, HttpResponse
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib import messages

from website.models import Customer
from website.forms.customers import CustomerForm

def create_customer_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = CustomerForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Customer successfully created!')
            return redirect('index_customer')
        return render(request, 'customers/create.html', { 'form': form })

    return render(request, 'customers/create.html', { 'form': CustomerForm() })

def update_customer_view(request: HttpRequest, customer_id: int) -> HttpResponse:
    customer = get_object_or_404(Customer, pk=customer_id)

    if request.method == 'POST':
        form = CustomerForm(data=request.POST, files=request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('index_customers')
        
        render(request, 'customers/update.html', {
            'customer': customer,
            'form': form,
        })
    
    return render(request, 'customers/update.html', {
        'customer': customer,
        'form': CustomerForm(instance=customer)
    }) 

def index_customers_view(request: HttpRequest) -> HttpResponse:
    customers = Customer.objects.all().order_by('-id')
    paginated_customers = Paginator(customers, 10)
    page_number = request.GET.get('page')
    page_customers = paginated_customers.get_page(page_number)

    context = {'customers': customers, 'page_customers': page_customers }
    return render(request, 'customers/index.html', context)

def show_customer_view(request: HttpRequest, customer_id: int) -> HttpResponse:
    customer = get_object_or_404(Customer, pk=customer_id)
    customer_initials = customer.first_name[0] + customer.last_name[0]

    context = { 'customer': customer, 'customer_initials': customer_initials }
    return render(request, 'customers/show.html', context)

def delete_customer_view(request: HttpRequest, customer_id: int) -> HttpResponse:
    customer = get_object_or_404(Customer, pk=customer_id)
    customer.delete()
    return redirect('index_customers')

def search_customer_view(request: HttpRequest) -> HttpResponse:
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

    context = { 'customers': customers, 'page_customers': page_customers }
    return render(request, 'customers/index.html', context)
    

