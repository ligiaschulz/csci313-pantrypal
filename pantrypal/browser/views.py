from django.shortcuts import render
from recipe.models import Recipe, Category, Ingredient
from .forms import SearchForm

def browse_all(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        cat_id = '0'
        ing_ids = []
        if form.is_valid():
            cat_id = form.cleaned_data["category"]
            for ing in form.cleaned_data["ingredient"]:
                ing_ids.append(ing)
        recipe_list = Recipe.objects.all()
        if cat_id != '0': 
            selected_category=Category.objects.get(pk=cat_id)
            recipe_list = recipe_list.filter(category=selected_category)
        for id in ing_ids:
            if id != '0':
                selected_ingredient = Ingredient.objects.get(pk=id)
                recipe_list = recipe_list.filter(ingredients = selected_ingredient)       
    else:
        recipe_list = Recipe.objects.all()
        form = SearchForm()
    context = {'recipe_list':recipe_list, 'form': form}
    return render(request, 'browser/browse.html', context=context)

