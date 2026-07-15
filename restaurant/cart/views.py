from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import CartItem
from .serialize import CartItemSerializer

class CartItemListCreateView(generics.ListCreateAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CartItem.objects.filter(username=self.request.user.username)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
class CartItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CartItem.objects.filter(username=self.request.user.username)