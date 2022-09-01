from django.shortcuts import render

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ChangePasswordSerializer, RegisterSerializer
from .models import CustomUser
from rest_framework import generics, status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import update_last_login


#Class based view to register user
class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class LoginWithEmail(APIView):
    permission_classes = (AllowAny,)
    
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        
        user = CustomUser.objects.filter(email = email).first()
        
        if user.check_password(password):               # I will checking the user password here.
            token = RefreshToken.for_user(user)         # generating the JWT token for user.
            update_last_login(None, user)               # updating the Last login of user.
                
            response = {
                'message': 'User logged in successfully',
                'access': str(token.access_token),
                'referesh_token':str(token),
            }
            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response("Didn't Match otp please try again", status=status.HTTP_400_BAD_REQUEST)
        


# Only logged in user can access the API
class ChangePasswordView(generics.UpdateAPIView):
    
    queryset = CustomUser.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer