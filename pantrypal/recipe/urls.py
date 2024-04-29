from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipe_detail, name='recipe_detail'),
    path('create/', views.RecipeCreate.as_view(), name='recipe-create'),
]
