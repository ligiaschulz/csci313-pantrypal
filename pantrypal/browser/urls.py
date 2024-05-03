from django.urls import path
from . import views

urlpatterns = [
    path('', views.browse_all, name='browse-all'),
    path('shopping-list/',views.shopping_list, name='shopping-list'),
]
