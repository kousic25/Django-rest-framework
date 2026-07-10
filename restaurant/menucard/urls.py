from django.urls import path
from .views import (
    CategoryListCreateView,
    CategoryDetailView,
    MenuItemListCreateView,
    MenuItemDetailView,
    MenuItemOptionListCreateView,
    MenuItemOptionDetailView,)

urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('menu-items/', MenuItemListCreateView.as_view(), name='menuitem-list'),
    path('menu-items/<int:pk>/', MenuItemDetailView.as_view(), name='menuitem-detail'),
    path('menu-item-options/', MenuItemOptionListCreateView.as_view(), name='menuitemoption-list'),
    path('menu-item-options/<int:pk>/', MenuItemOptionDetailView.as_view(), name='menuitemoption-detail'),
]