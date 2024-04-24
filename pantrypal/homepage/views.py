from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def index(request):
    user_list = User.objects.all()
    return render(request, 'homepage/index.html')

def account_view(request,pk):
    if request.user.is_authenticated:
        current_user = User.objects.get(pk=pk)
        return render(request, 'homepage/account.html', {'usr' : current_user})
    else:
        messages.success(request, 'you need to be logged in to see account details')
        return redirect('home')