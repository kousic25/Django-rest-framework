from django.urls import path
from .views import (
    OrderListCreateView,
    OrderDetailView,
    OrderItemListCreateView,
    OrderItemDetailView,)

urlpatterns = [
    path('', OrderListCreateView.as_view(), name='order-list-create'),
    path('<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('items/', OrderItemListCreateView.as_view(), name='orderitem-list-create'),
    path('items/<int:pk>/', OrderItemDetailView.as_view(), name='orderitem-detail'),
]