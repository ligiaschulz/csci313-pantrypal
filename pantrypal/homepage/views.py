from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from recipe.models import Saved_recipe, Recipe

# Create your views here.
def index(request):
    return render(request, 'homepage/index.html')

def account_view(request):
    if request.user.is_authenticated:
        saved_recipe_list = Saved_recipe.objects.filter(user_id = request.user)
        context = {'recipe' : saved_recipe_list}
        return render(request, 'homepage/account.html', context= context)
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

def update(request):
    pass

def remove_saved_recipe(request, pk):
    if request.user.is_authenticated:
        recipe = Recipe.objects.get(pk=pk)
        saved_recipe= Saved_recipe.objects.get(user_id = request.user, recipe_id=recipe)
        saved_recipe.delete()
        messages.success(request, "Succesfully removed recipe.")
        return redirect(account_view)
    else:
        messages.success(request, 'You must be logged in to make account changes')
        return redirect(index)