from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.views import generic
from .models import Recipe
from django.contrib.auth.decorators import login_required

# Create your views here.
def recipe_detail(request):
    user_list = User.objects.all()
    instructions = {
        "instructions" : ['basic instructions']
    }
    ingredients = {
        "ingredients" : ['eggs', 'milk'],

    }
    return render(request,'recipe/recipe.html',ingredients)
    

class RecipeCreate(generic.CreateView):
    model = Recipe
    fields=['recipe_name','category', 'servings','ingredients','recipe_instructions']
    

    
    context = {'instructions':instructions, 'ingredients': ingredients}
    
    return render(request,'recipe/recipe.html', context=context)
