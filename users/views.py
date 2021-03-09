from django.shortcuts import render

from .models import Profile,User


from .serializers import (
    ProfileCreateSerializer,
    ProfileSerializer,
    UserSerializer,
    UserCreateSerializer,
    UserUpdateSerializer,
)
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import (
    IsAuthenticated
)
from .permissions import (
    IsOwnerOrReadOnly
)

from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView,
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView,
    

)
##### User #####
class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
    lookup_url_kwarg = 'username'
    permission_classes = [IsAuthenticated]


class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    lookup_field = 'username'
    lookup_url_kwarg = 'username'
    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]


class UserDeleteView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
    lookup_url_kwarg = 'username'
    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]


#### Profile #####

class ProfileDetailView(RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


    lookup_field = 'user__username'
    lookup_url_kwarg = 'username'
    