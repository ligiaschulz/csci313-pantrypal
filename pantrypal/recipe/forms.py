from django import forms
from recipe.models import Category, Ingredient, UNITS



class NewRecipeForm(forms.Form):  
    categories={}
    ingredients={}
    for item in Ingredient.objects.all():
        ingredients[item.pk] = item.ingredient_name
    for item in Category.objects.all():
        categories[item.pk] = item.category_name
    recipe_name = forms.CharField(label="Recipe Name", max_length=100)
    category = forms.MultipleChoiceField(label="Category", choices=categories)
    servings = forms.IntegerField(label="Servings")
    instructions = forms.CharField(label="Instructions", max_length=500, widget=forms.Textarea)

class RecipeLineForm(forms.Form):
    ingredients={}
    for item in Ingredient.objects.all():
        ingredients[item.pk] = item.ingredient_name
    ingredient = forms.ChoiceField(label="Ingredient",  choices=ingredients)
    amount = forms.FloatField()
    unit = forms.ChoiceField(label = "Unit", choices=UNITS)

RecipeLineFormSet = forms.formset_factory(RecipeLineForm)

class NotesForm(forms.Form):
    notes = forms.CharField(max_length=500, widget=forms.Textarea)