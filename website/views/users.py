from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib import messages

from website.forms.users import UserRegisterForm

def register_user(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration done successfully!')
            return redirect('customers')
        return render(request, 'users/register.html', { 'form': form })

    return render(request, 'users/register.html', { 'form': UserRegisterForm() })