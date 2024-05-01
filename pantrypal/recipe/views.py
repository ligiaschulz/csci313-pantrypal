from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.views import generic
from .models import Recipe, Recipe_line
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import RecipeLineForm, NewRecipeForm

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

def create_recipe(request):
    if request.method == "POST":
        form = NewRecipeForm(request.POST)
        if form.is_valid():
            categories = form.cleaned_data['category']
            recipe_name = form.cleaned_data['recipe_name']
            instructions = form.cleaned_data['instructions']
            servings = form.cleaned_data['servings']
            newRecipe = Recipe(recipe_name=recipe_name, recipe_instructions=instructions, servings=servings)
            newRecipe.save() 
            for id in categories:
                cat = Category.objects.get(pk=id)
                newRecipe.category.add(cat)
            newRecipe.save()
            return redirect('ingredient/%d'%(newRecipe.pk))
    else:     
        form = NewRecipeForm()
    context = {'form': form}
    return render(request, 'recipe/recipe_line_form.html', context=context)

def create_recipeline(request, pk):
    if request.method == "POST":
        form = RecipeLineForm(request.POST)
        if form.is_valid():
            ingredient_id = form.cleaned_data["ingredient"]
            ingredient = Ingredient.objects.get(pk=ingredient_id)
            amount = form.cleaned_data["amount"]
            unit = form.cleaned_data["unit"]
            recipe = Recipe.objects.get(pk=pk)
            newLine = Recipe_line(ingredient_id=ingredient, recipe_id=recipe, amount=amount, unit=unit) 
            newLine.save()      
    form = RecipeLineForm()
    context = {'form': form}
    return render(request, 'recipe/recipe_line_form.html', context=context)


class Recipe_LineCreate(generic.CreateView):
    model = Recipe_line
    fields = ['recipe_id','ingredient_id','amount','unit']
    success_url = reverse_lazy('recipe-ingredients')
    
    

    
    
