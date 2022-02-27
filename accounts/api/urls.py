from django.urls import path
from .views import (
    CustomUserCreateView, BlackListTokenView, ChangePasswordView)
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView


app_name = 'api_users'

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', CustomUserCreateView.as_view(), name='create_user'),
    path('logout/blacklist/', BlackListTokenView.as_view(), name='blacklist'),
    path('change_password/<int:pk>/', ChangePasswordView.as_view(), 
                                    name='change_password'),
   # path('update_profile/<int:pk>/', UpdateProfileView.as_view(), name='auth_update_profile'),
]
