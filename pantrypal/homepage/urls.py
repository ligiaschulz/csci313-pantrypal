from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/<int:pk>/', views.account_view, name='accounts'),
]
