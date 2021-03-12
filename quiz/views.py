from django.shortcuts import render, get_object_or_404

from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django.contrib.auth import get_user_model
from django.views import View
from django.views.generic.list import ListView

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

from .serializers import QuizListSerializer, QuizRetrieveSerializer
from .permissions import IsAuthor, IsStaff


User = get_user_model()




class IndexView(View):

    def get(self,request):
        quizzes = Quiz.objects.filter(status=3)
        urls = []
        for quiz in quizzes:
            urls.append(quiz.get_absolute_url())
        context = {
            'hello':'world',
            'quiz_data' : zip(quizzes,urls)

        }
        return render(request,'quiz/index.html',context=context)
        

class QuizList(ListAPIView):
    ''' 
        Staff can list the quizzes they have created
    '''
    queryset = Quiz.objects.all()
    permission_classes = [IsAuthenticated, IsStaff]
    serializer_class = QuizListSerializer

    def get_queryset(self):
        user = self.request.user
        print(user)
        if user.is_superuser:
            return Quiz.objects.all()
        obj = Quiz.objects.filter(author=user)
        print(obj)
        return obj


class UserQuizList(ListAPIView):
    ''' 
        Normal user can view the all the public quiz or
        private quiz if they have permission
    '''
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
    
