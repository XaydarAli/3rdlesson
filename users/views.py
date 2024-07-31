from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

class UserLoginView(View):
    def get(self, request):
        return render(request, 'auth/login.html')

    def post(self, request):
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            messages.success(request, 'You are successfully logged in.')
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password.')
            return render(request, 'auth/login.html')

class UserRegisterView(View):
    def get(self, request):
        return render(request, 'auth/register.html')

    def post(self, request):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            new_user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email)
            new_user.set_password(password1)
            new_user.save()
            messages.success(request, "You successfully registered")
            return redirect('auth-login')
        else:
            messages.warning(request, "Passwords don't match")
            return render(request, 'auth/register.html')


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, "You have been successfully logged out.")
        return redirect('index')



