from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipe_detail, name='recipe_detail'),
]
