from django.shortcuts import render, get_object_or_404

from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django.contrib.auth import get_user_model


from rest_framework.views import APIView
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView
)

from .models import (
    Quiz,
    Problem,
    Option,
    ScoreBoard
)

from .serializers import QuizListSerializer,QuizRetrieveSerializer



User = get_user_model()

class QuizList(ListAPIView):
    queryset = Quiz.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = QuizListSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Quiz.objects.all()
            
        return Quiz.objects.filter(author=user)

class QuizRetrieveView(RetrieveAPIView):
    queryset = Quiz.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = QuizRetrieveSerializer

    # def get_object(self):
    #     queryset = self.get_queryset()
    #     filter = {}
    #     field = self.lookup_field
    #     filter[field] = self.kwargs[field]

    #     obj = get_object_or_404(queryset, **filter)
    #     self.check_object_permissions(self.request, obj)
        
    #     return obj
