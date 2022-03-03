from django.urls import path
from .views import SignUpView, UserUpdateView, ChangePassword

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('my_profile/<slug:slug>', UserUpdateView.as_view(), name='my_profile'),
    path('change-password/', ChangePassword.as_view(), name="change_password"),

    
]

app_name = 'users'
