from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from website.models import Customer as CustomerModel

def list_customers(request: HttpRequest) -> HttpResponse:
    customers = CustomerModel.objects.all().order_by('-id')
    context = { 'customers': customers }
    return HttpResponse(render(request, 'index.html', context))