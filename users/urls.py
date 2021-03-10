
from django.urls import path,include

from .views import (
    UserRegisterView,
    UserLogoutView

)
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', UserRegisterView.as_view()),
    path('login/', obtain_auth_token),
    path('logout/', UserLogoutView.as_view()),
]
