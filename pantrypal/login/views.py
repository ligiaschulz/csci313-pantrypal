from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm

def login_user(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been authenticated and logged in successfully')
            return redirect('../../homepage/')
        else:
            messages.success(request, 'Login failed, try again')
            return redirect('login')
    else:
        return render(request, 'login/login.html', {})
    
def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully')
    return redirect ('index')

def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            username  = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username = username, password = password)
            login(request, user)
            messages.success(request, 'You were registered and logged in successfully')
            return redirect('index')
        
    else:
        form = SignUpForm()
    return render(request, 'login/register.html', {'form' : form})

def update(request):
    pass