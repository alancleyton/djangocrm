from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from website.forms.users import UserCreateForm

def create(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'users/create.html', { 'form': form })
        
    return render(request, 'users/create.html', { 'form': UserCreateForm() })