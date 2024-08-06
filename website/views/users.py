from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib import auth
from django.contrib import messages

from website.forms.users import UserRegisterForm, UserLoginForm

def user_register_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration done successfully!')
            return redirect('user_login')
        return render(request, 'users/register.html', { 'form': form })

    return render(request, 'users/register.html', { 'form': UserRegisterForm() })

def user_login_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect('customers')
        else:
            messages.error(request, 'Invalid credentials, please try again!')
        return render(request, 'users/login.html', { 'form': form })

    return render(request, 'users/login.html', { 'form': UserLoginForm() })

def user_logout_view(request: HttpRequest) -> HttpResponse:
    auth.logout(request)
    return redirect('user_login')


