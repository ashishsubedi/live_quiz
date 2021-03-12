from django.contrib import admin
from django.urls import path,include

from .views import (
    QuizList,
    QuizRetrieveView,
    IndexView
)

urlpatterns = [
    path('', IndexView.as_view() ,name='index'),
    path('api/quiz/',include('quiz.urls_api')),


]
