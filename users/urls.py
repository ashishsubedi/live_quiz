
from django.urls import path,include

from .views import (
    UserRegisterView,
    UserLogoutView,
    CustomAuthToken,
    UserInformationFromTokenView

)
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', UserRegisterView.as_view(),name='user-register'),
    path('login/', CustomAuthToken.as_view(),name='user-login'),
    path('logout/', UserLogoutView.as_view(),name='user-logout'),
    path('info/', UserInformationFromTokenView.as_view(),name='user-info'),
]
