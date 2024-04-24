from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'homepage/index.html')
<<<<<<< Updated upstream
=======

def account_view(request,pk):
    if request.user.is_authenticated:
        current_user = User.objects.get(pk=pk)
        return render(request, 'homepage/account.html', {'usr' : current_user})
    else:
        messages.success(request, 'you need to be logged in to see account details')
        return redirect('home')
>>>>>>> Stashed changes
