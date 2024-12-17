from django.shortcuts import render
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework import generics,status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .models import *
from .serializers import *

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self,request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data.get('email')
        password = serializer.validated_data.get('password')

        user = authenticate(email=email,password=password)
        user = User.objects.get(email=email)
        # if not user:
        #     raise AuthenticationFailed('Invalid credentials')
        if user.is_superuser:
           
            token = get_tokens_for_user(user)
            return Response({
                "message": "Login successful",
                "token": token,
                "user_email": user.email,
                "user":"Admin"
            }, status=status.HTTP_200_OK)
        
        elif user.is_librarian:
            token = get_tokens_for_user(user)
            return Response({
                "message": "Login successful",
                "token": token,
                "user_email": user.email,
                "user":"Librarian"
            }, status=status.HTTP_200_OK)
        
        elif user.is_officestaff:
            token = get_tokens_for_user(user)
            return Response({
                "message": "Login successful",
                "token": token,
                "user_email": user.email,
                "user":"Office Staff"
                }, status=status.HTTP_200_OK)


        



