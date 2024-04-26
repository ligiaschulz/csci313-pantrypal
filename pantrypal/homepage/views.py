from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'homepage/index.html')

def account_view(request):
    if request.user.is_authenticated:
        
        return render(request, 'homepage/account.html',)
    else:
        messages.success(request, 'you need to be logged in to see account details')
        return redirect('home')
    
def delete(request):
    if request.user.is_authenticated:
        del_user = request.user
        del_user.delete()
        return redirect('index')
    else:
        messages.success(request, 'you need to be logged in to delete your user')
        return redirect('index')        