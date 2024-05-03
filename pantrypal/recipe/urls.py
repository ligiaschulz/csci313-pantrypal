from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.RecipeAddView.as_view(), name='recipe-create'),
    path('<int:recipe_id>/', views.recipe_detail, name='recipe-detail'),
]
