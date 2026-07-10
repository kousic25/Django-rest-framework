from django.urls import path
from .views import (
    UserListCreateView,
    UserDetailView,
    UserAddressListCreateView,
    UserAddressDetailView,
    RegisterView,
    LoginView,
    LogoutView,
    EmailVerificationView, )

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('addresses/', UserAddressListCreateView.as_view(), name='address-list'),
    path('addresses/<int:pk>/', UserAddressDetailView.as_view(), name='address-detail'),
    path('register/', RegisterView.as_view(), name='register'),
    path('verify-email/', EmailVerificationView.as_view(), name='verify-email'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]