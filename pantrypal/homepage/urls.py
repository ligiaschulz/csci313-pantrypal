from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', views.account_view, name='accounts'),
    path('delete/', views.delete, name="delete"),
]
