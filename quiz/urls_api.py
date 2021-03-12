from django.contrib import admin
from django.urls import path,include

from .views import (
    QuizList,
    QuizRetrieveView,
    IndexView
)

urlpatterns = [
    path('list/', QuizList.as_view(),name='quiz_list'),
    path('<pk>/', QuizRetrieveView.as_view(),name='quiz_detail'),

]
