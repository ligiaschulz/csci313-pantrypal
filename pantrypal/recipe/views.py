from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.views import generic
from .models import Recipe
from django.contrib.auth.decorators import login_required

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

class RecipeCreate(generic.CreateView):
    model = Recipe
    fields=['recipe_name','category', 'servings','ingredients','recipe_instructions']