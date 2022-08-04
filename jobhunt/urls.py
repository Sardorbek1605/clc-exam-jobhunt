from django.contrib import admin
from django.urls import path, include
from .views import CountsViewSet, CategoriesListViewSet

urlpatterns = [
    path('counts/', CountsViewSet.as_view()),
    path('categories/', CategoriesListViewSet.as_view()),
]