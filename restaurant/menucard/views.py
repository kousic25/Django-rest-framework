from rest_framework import generics
from .models import Category, MenuItem, MenuItemOption
from .serialize import (
    CategorySerializer,
    MenuItemSerializer,
    MenuItemOptionSerializer,)

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class MenuItemListCreateView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class MenuItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class MenuItemOptionListCreateView(generics.ListCreateAPIView):
    queryset = MenuItemOption.objects.all()
    serializer_class = MenuItemOptionSerializer

class MenuItemOptionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItemOption.objects.all()
    serializer_class = MenuItemOptionSerializer