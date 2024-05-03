from django.db import models
from django.conf import settings


UNITS=(('', 'None'),('t','tsp'),('T','Tbsp'),('c','cups'),('o','ounces'))

class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=50)
    def __str__(self):
        return self.ingredient_name

class Category(models.Model):
    category_name = models.CharField(max_length=50)
    def __str__(self):
        return self.category_name

class Recipe(models.Model):
    recipe_name = models.CharField(max_length=100)
    recipe_instructions = models.TextField()
    servings = models.IntegerField()

    #field for ingredients associated with a particular recipe
    ingredients=models.ManyToManyField(Ingredient, through="Recipe_line")

    creator=models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL, related_name="owned_recipes")
    category=models.ManyToManyField(Category)

    #field for users who have saved the recipe
    users=models.ManyToManyField(settings.AUTH_USER_MODEL, through="Saved_recipe")

    def __str__(self):
        return self.recipe_name

class Saved_recipe(models.Model):
    recipe_id=models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user_id=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    notes=models.TextField()

class Recipe_line(models.Model):
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient_id=models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    amount=models.FloatField(null=True, blank=True)
    unit=models.CharField(max_length=1,choices=UNITS,null=True,blank=True)