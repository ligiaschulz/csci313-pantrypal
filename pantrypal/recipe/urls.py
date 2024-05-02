from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipe_detail, name='recipe_detail'),
    path('create/', views.create_recipe, name='recipe-create'),
    path('create/ingredient/<int:pk>', views.create_recipeline, name='recipe-ingredients'),
    path('<int:recipe_id>/', views.recipe_detail, name='recipe-ingredients'),
]
