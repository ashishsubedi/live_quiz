from django.contrib import admin
from django.urls import path,include

from .views import (
    QuizList,
    QuizRetrieveView
)

urlpatterns = [
    path('', QuizList.as_view(),name='quiz_list'),
    path('<pk>/', QuizRetrieveView.as_view(),name='quiz_detail'),

]
