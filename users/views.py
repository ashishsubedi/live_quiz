from django.contrib.auth import get_user_model
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions,status

from .serializers import UserSerializer

User = get_user_model()

class UserRegisterView(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    def post(self,request):
        '''
            Create new user
        '''
        data = request.data
        print(data)
        serializer = UserSerializer(data=data)
        
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            'status': status.HTTP_200_OK,
            'data':serializer.data
        })
    
class UserLogoutView(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request):
        '''
            Logout user
        '''
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
        
    

        

