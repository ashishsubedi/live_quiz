
from django.urls import path, include

from .views import (
    UserCreateView,
    UserDetailView,
    UserUpdateView,
    UserDeleteView,

    ProfileDetailView

)

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    
    path('register/',UserCreateView.as_view(),name='user-register'),
    path('login/',obtain_auth_token,name='user-login'),
    path('<str:username>/',UserDetailView.as_view(),name='user-detail'),
    path('<str:username>/update/',UserUpdateView.as_view(),name='user-update'),
    path('<str:username>/delete/',UserDeleteView.as_view(),name='user-delete'),
    
    path('profile/<str:username>/',ProfileDetailView.as_view(),name='user-profile-detail'),

]

urlpatterns += [
    path('api-token-auth/', obtain_auth_token)
]
