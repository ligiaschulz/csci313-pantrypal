from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.views import generic
from .models import Recipe, Recipe_line, Ingredient
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

# Create your views here.
def recipe_detail(request):
    recipelist = Recipe.objects.all()
    ingredients = Ingredient.objects.all()
   
    context = {'ingredients':ingredients}
    return render(request,'recipe/recipe.html',context)
    

class RecipeCreate(generic.CreateView):
    model = Recipe
    fields=['recipe_name','category', 'servings','recipe_instructions']
    success_url = reverse_lazy('recipe-ingredients')

class Recipe_LineCreate(generic.CreateView):
    model = Recipe_line
    fields = ['recipe_id','ingredient_id','amount','unit']
    success_url = reverse_lazy('recipe-ingredients')
    
    

    
    
