from django.urls import path
from .views import (
    SignUpAPIView,
    BlackListTokenView,
    ChangePasswordAPIView,
    UserUpdateAPIView,
)
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView


app_name = "api_users"

urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("login/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("register/", SignUpAPIView.as_view(), name="create_user"),
    path("logout/blacklist/", BlackListTokenView.as_view(), name="blacklist"),
    path(
        "change_password/<int:pk>/",
        ChangePasswordAPIView.as_view(),
        name="change_password",
    ),
    path(
        "update_profile/<int:pk>/", UserUpdateAPIView.as_view(), name="update_profile"
    ),
]
