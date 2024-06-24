from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def list_customers(request: HttpRequest) -> HttpResponse:
    return HttpResponse(render(request, 'index.html', {}))