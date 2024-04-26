from django.urls import path
from . import views

urlpatterns = [
    path('', views.browse_all, name='browse-all'),
    path('category<int:pk>/', views.category_filter, name='category-filter'),
]
