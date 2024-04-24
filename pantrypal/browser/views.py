from django.shortcuts import render
from django.views import generic
from recipe.models import Recipe


class RecipeListView(generic.ListView):
    model = Recipe
    template_name='browser/browse.html'