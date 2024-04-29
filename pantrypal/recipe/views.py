from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def recipe_detail(request):
    user_list = User.objects.all()
    instructions = {
        "instructions" : ['basic instructions']
    }
    ingredients = {
        "ingredients" : ['eggs', 'milk'],

    }
    
    context = {'instructions':instructions, 'ingredients': ingredients}
    
    return render(request,'recipe/recipe.html', context=context)
