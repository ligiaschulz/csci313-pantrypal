from django.shortcuts import render
from django.views import generic
from recipe.models import Recipe


class RecipeListView(generic.ListView):
    model = Recipe
    template_name='browser/browse.html'

def filter(request):
    recipe_list = Recipe.objects.all()
    context = {'recipe_list':recipe_list}
    return render(request, 'browser/browse.html', context=context)