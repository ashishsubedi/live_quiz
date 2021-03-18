from django.contrib.auth import get_user_model
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions,status
  

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token



from .serializers import UserCreateSerializer,UserSerializer

User = get_user_model()

class UserRegisterView(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    def post(self,request):
        '''
            Create new user
        '''
        data = request.data
        print(data)
        serializer = UserCreateSerializer(data=data)
        
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            'status': status.HTTP_200_OK,
            'data':serializer.data
        })
    
class UserLogoutView(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]
    def get(self,request):
        '''
            Logout user
        '''
        try:
            request.user.auth_token.delete()
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    
class UserInformationFromTokenView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]

    def post(self,request):
        '''
            Get  user information
        '''
        try:

            data = Token.objects.get(key=request.data['token'])

            serializer = UserSerializer(data.user)

            return Response({
                'token': data.key,
                'user': serializer.data
            })
        except:
            return Response({
                'detail': "Error getting user information"
            },status=status.HTTP_400_BAD_REQUEST)
class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                        context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'username': user.username,
            'email': user.email,
            'name': user.first_name
        })