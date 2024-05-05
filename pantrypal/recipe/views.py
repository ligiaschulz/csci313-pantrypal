from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.views import generic
from .models import Recipe, Recipe_line, Category, Ingredient, Saved_recipe
from django.contrib.auth.decorators import login_required
from .forms import RecipeLineForm, NewRecipeForm, RecipeLineFormSet, NotesForm


# Create your views here.
def recipe_detail(request, recipe_id):
    try:
        recipe = get_object_or_404(Recipe, pk=recipe_id)
        ingredients = Recipe_line.objects.filter(recipe_id=recipe)
        recipe_is_saved = False
        saved_recipe=Saved_recipe()
        if request.user.is_authenticated:
            recipe_is_saved = has_saved_recipe(recipe, request.user)
            if recipe_is_saved:
                saved_recipe = Saved_recipe.objects.get(user_id=request.user, recipe_id=recipe)
        if request.method == "POST":
            if recipe_is_saved:
                form = NotesForm(request.POST)
                if form.is_valid():
                    notes=form.cleaned_data["notes"]
                    saved_recipe.notes=notes
                    saved_recipe.save(update_fields=["notes"])
                    messages.success(request, "Notes have been updated.")
            else:
                messages.success(request, "You must be logged and have the recipe saved to add notes.")

        form = NotesForm(initial={'notes':saved_recipe.notes})          
        context = {
            'recipe': recipe,
            'ingredients': ingredients,
            'recipe_is_saved': recipe_is_saved,
            'form': form
        }
        return render(request, 'recipe/recipe.html', context)
        
    except Recipe.DoesNotExist:
        return None
    

def add_notes(request, recipe_id):
    if request.user.is_authenticated:
        #add the notes
        return redirect('/recipe/%d'%recipe_id)
    else:
        messages.success(request, "You must be logged in to add notes.")
        return redirect('/recipe/%d'%recipe_id)


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
                    newLine = Recipe_line(ingredient_id=ingredient, recipe_id=newRecipe, amount=amount, unit=unit) 
                    newLine.save()
                return redirect('/recipe/%d'%newRecipe.pk)
            return self.render_to_response({'recipe_form': recipeForm, 'recipe_lines': lineFormset})
        else:
            messages.success(self.request, "You must be logged in to create a recipe.")
            return redirect('/homepage')  

def add_saved_recipe(request, pk):
    if request.user.is_authenticated:
        recipe = Recipe.objects.get(pk=pk)
        saved_recipe= Saved_recipe(user_id = request.user, recipe_id=recipe)
        saved_recipe.save()
        messages.success(request, "Succesfully saved recipe.")
        return redirect('/recipe/%d'%pk)
    else:
        messages.success(request, 'You must be logged in to save a recipe')
        return redirect('/recipe/%d'%pk)
    

def has_saved_recipe(recipe, user):
    saved_recipe = Saved_recipe.objects.filter(user_id=user, recipe_id=recipe).exists()
    return saved_recipe

    
