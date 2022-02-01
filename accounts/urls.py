from django.urls import path
from .views import SignUpView, UserUpdateView, login_view, UpdatePassword

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('my_profile/<slug:slug>', UserUpdateView.as_view(), name='my_profile'),
    path('login/', login_view, name='login'),
    path('change-password/', UpdatePassword.as_view(), name="change_password"),

    
]

app_name = 'users'
