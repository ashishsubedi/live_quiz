from django.shortcuts import render

from rest_framework.permissions import IsAdminUser
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

from .serializers import QuizListSerializer



User = get_user_model()

class QuizList(ListAPIView):
    queryset = Quiz.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = QuizListSerializer
