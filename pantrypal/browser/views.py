from django.shortcuts import render
from django.views import generic
from recipe.models import Recipe, Category

def browse_all(request):
    recipe_list = Recipe.objects.all()
    category_list = Category.objects.all()
    context = {'recipe_list':recipe_list, 'category_list':category_list}
    return render(request, 'browser/browse.html', context=context)

def category_filter(request, pk):
    selected_category=Category.objects.get(pk=pk)
    recipe_list = Recipe.objects.filter(category=selected_category)
    category_list = Category.objects.all()
    context = {'recipe_list':recipe_list, 'category_list':category_list, 'selected_category':selected_category}
    return render(request, 'browser/browse.html', context=context)