from django.contrib import admin
from .models import Recipe, Category, Ingredient, Recipe_line, Saved_recipe

admin.site.register(Category)
admin.site.register(Ingredient)
admin.site.register(Recipe_line)
admin.site.register(Saved_recipe)

# Register your models here.
class Recipe_lineInline(admin.TabularInline):
    model = Recipe_line

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines=[Recipe_lineInline]