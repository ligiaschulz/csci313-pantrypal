from django import forms
from recipe.models import Category, Ingredient

class SearchForm(forms.Form):
    
    categories={0: 'None'}
    ingredients={0: 'None'}
    for item in Ingredient.objects.all():
        ingredients[item.pk] = item.ingredient_name
    for item in Category.objects.all():
        categories[item.pk] = item.category_name
    category = forms.ChoiceField(label="Category", choices=categories)
    ingredient = forms.MultipleChoiceField(label="Ingredients",  choices=ingredients)
    exclude = forms.MultipleChoiceField(label="Ingredients Excluded", choices=ingredients)

    
    
    
