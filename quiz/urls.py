from django.contrib import admin
from django.urls import path,include

from .views import QuizList

urlpatterns = [
    path('', QuizList.as_view()),

]
