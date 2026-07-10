from django.contrib.auth import authenticate
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User, UserAddress
from .serialize import UserSerializer, UserAddressSerializer

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserAddressListCreateView(generics.ListCreateAPIView):
    queryset = UserAddress.objects.all()
    serializer_class = UserAddressSerializer

class UserAddressDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserAddress.objects.all()
    serializer_class = UserAddressSerializer

class RegisterView(APIView):

    def post(self, request):

        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                {
                    "message": "User Registered Successfully",
                    "user": serializer.data
                },
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class LoginView(APIView):

    def post(self, request):

        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(
            username=username,
            password=password
        )

        if user is not None:

            refresh = RefreshToken.for_user(user)

            return Response(
                {
                    "message": "Login Successful",

                    "access_token": str(refresh.access_token),

                    "refresh_token": str(refresh),

                    "user": {
                        "id": user.id,
                        "username": user.username,
                        "first_name": user.first_name,
                        "last_name": user.last_name,
                        "email": user.email,
                        "phone_number": user.phone_number,
                        "role": user.role,
                    }
                },
                status=status.HTTP_200_OK
            )

        return Response(
            { "message": "Invalid Username or Password" },
            status=status.HTTP_401_UNAUTHORIZED )

class EmailVerificationView(APIView):

    def post(self, request):

        email = request.data.get("email")

        if not email:
            return Response(
                {
                    "message": "Email is required"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        if User.objects.filter(email=email).exists():
            return Response(
                {
                    "message": "Email already exists",
                    "available": False
                },
                status=status.HTTP_200_OK
            )

        return Response(
            {
                "message": "Email is available",
                "available": True
            },
            status=status.HTTP_200_OK
        )

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):

        try:
            refresh_token = request.data.get("refresh_token")

            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(
                {
                    "message": "Logout Successful"
                },
                status=status.HTTP_205_RESET_CONTENT
            )

        except Exception:
            return Response(
                {
                    "message": "Invalid or Expired Refresh Token"
                },
                status=status.HTTP_400_BAD_REQUEST
            )


