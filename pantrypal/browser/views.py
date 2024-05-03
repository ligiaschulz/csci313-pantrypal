from django.shortcuts import render, redirect
from recipe.models import Recipe, Category, Ingredient, Recipe_line
from .forms import SearchForm, ShoppingListForm

def browse_all(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        cat_id = '0'
        ing_ids = []
        exc_ids = []
        if form.is_valid():
            cat_id = form.cleaned_data["category"]
            for ing in form.cleaned_data["ingredient"]:
                ing_ids.append(ing)
            for id in form.cleaned_data["exclude"]:
                exc_ids.append(id)
        recipe_list = Recipe.objects.all()
        if cat_id != '0': 
            selected_category=Category.objects.get(pk=cat_id)
            recipe_list = recipe_list.filter(category=selected_category)
        for id in ing_ids:
            if id != '0':
                selected_ingredient = Ingredient.objects.get(pk=id)
                recipe_list = recipe_list.filter(ingredients = selected_ingredient)     
        for id in exc_ids:
            if id != '0':
                selected_ingredient = Ingredient.objects.get(pk=id)
                recipe_list = recipe_list.exclude(ingredients = selected_ingredient)  
    else:
        recipe_list = Recipe.objects.all()
        form = SearchForm()
    context = {'recipe_list':recipe_list, 'form': form}
    return render(request, 'browser/browse.html', context=context)

def shopping_list(request):
    if request.method == "POST":
        saved_ingredients = []
        form = ShoppingListForm(request.POST)
        if form.is_valid():
            selected_recipes = form.cleaned_data['recipes']   
            for recipe in selected_recipes:
                ingredients = Recipe_line.objects.filter(recipe_id=recipe)
                for line in ingredients:
                    i = line.ingredient_id
                    saved_ingredients.append(i)
            saved_ingredients = list(dict.fromkeys(saved_ingredients))
            context = {'selected': selected_recipes, 'form': form, 'selected_ingredients':saved_ingredients} 
            return render(request, 'browser/shopping_list.html', context = context)
    else:
        form = ShoppingListForm()
    context = {'form':form}
    return render(request, 'browser/shopping_list.html', context = context)