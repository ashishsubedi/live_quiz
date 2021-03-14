from django.contrib import admin
from django.urls import path,include

from .views import (
    QuizList,
    QuizRetrieveView,
    IndexView,
    QuizAnswerVerify
)

urlpatterns = [
    path('list/', QuizList.as_view(),name='quiz_list'),
    path('quiz/check/', QuizAnswerVerify.as_view(),name='quiz_answer_verify'),
    path('<pk>/', QuizRetrieveView.as_view(),name='quiz_detail'),

]
