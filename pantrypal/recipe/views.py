from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def recipe_detail(request):
    user_list = User.objects.all()
    return render(request, 'recipe/recipe.html')

def ingredients_view(request):
    ingredients = {
        "ingredients" : ['eggs', 'milk'],

    }
    return render(request, 'recipe.html', ingredients)

def recipe_instructions(request):
    instructions = {
        "instructions" : ['basic instructions']
    }
    return render(request, 'recipe.html', instructions)
