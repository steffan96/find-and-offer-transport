from django.urls import path
from .views import SignUpView, UserUpdateView, LoginFormView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('my_profile/<int:pk>', UserUpdateView.as_view(), name='my_profile'),
    path('login/', LoginFormView.as_view(), name='login'),

    
]

app_name = 'users'