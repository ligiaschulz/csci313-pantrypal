from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def index(request):
    user_list = User.objects.all()
    return render(request, 'recipe/index.html')

