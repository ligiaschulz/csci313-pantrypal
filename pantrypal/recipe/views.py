from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.views import generic
from .models import Recipe, Recipe_line, Category, Ingredient, Saved_recipe
from django.contrib.auth.decorators import login_required
from .forms import RecipeLineForm, NewRecipeForm, RecipeLineFormSet


# Create your views here.
def recipe_detail(request, recipe_id):
    try:
        recipe = get_object_or_404(Recipe, pk=recipe_id)
        ingredients = Recipe_line.objects.filter(recipe_id=recipe)
        saved_recipe = Saved_recipe.objects.filter(recipe_id=recipe)
        if(saved_recipe == recipe_id):
            recipe_is_saved = True
        else:
            recipe_is_saved = False
        
        context = {
            'recipe': recipe,
            'ingredients': ingredients,
            'saved_recipe': saved_recipe,
            'recipe_is_saved':recipe_is_saved,
        }
        return render(request, 'recipe/recipe.html', context)
        
    except Recipe.DoesNotExist:
        return None
    



class RecipeAddView(generic.TemplateView):
    template_name = "recipe/recipe_form.html"
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            form = NewRecipeForm()
            formset = RecipeLineFormSet()
            return self.render_to_response({'recipe_form': form, 'recipe_lines': formset})
        else:
            messages.success(self.request, "You must be logged in to create a recipe.")
            return redirect('/homepage')
    
    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            recipeForm = NewRecipeForm(data = self.request.POST)
            lineFormset = RecipeLineFormSet(data = self.request.POST)
            recipe_valid = recipeForm.is_valid()
            line_valid = lineFormset.is_valid()
            if recipe_valid and line_valid:
                categories = recipeForm.cleaned_data['category']
                recipe_name = recipeForm.cleaned_data['recipe_name']
                instructions = recipeForm.cleaned_data['instructions']
                servings = recipeForm.cleaned_data['servings']
                creator = self.request.user
                newRecipe = Recipe(recipe_name=recipe_name, recipe_instructions=instructions, servings=servings, creator=creator)
                newRecipe.save()
                newRecipe.users.add(creator)
                for id in categories:
                    cat = Category.objects.get(pk=id)
                    newRecipe.category.add(cat)
                newRecipe.save()
                for form in lineFormset:
                    ingredient_id = form.cleaned_data["ingredient"]
                    ingredient = Ingredient.objects.get(pk=ingredient_id)
                    amount = form.cleaned_data["amount"]
                    unit = form.cleaned_data["unit"]
                    recipe = newRecipe
                    newLine = Recipe_line(ingredient_id=ingredient, recipe_id=recipe, amount=amount, unit=unit) 
                    newLine.save()
                return redirect('/homepage/accounts')
            return self.render_to_response({'recipe_form': recipeForm, 'recipe_lines': lineFormset})
        else:
            messages.success(self.request, "You must be logged in to create a recipe.")
            return redirect('/homepage')  

    
    

    
    
