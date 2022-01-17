from django.urls import path
from .views import SignUpView, UserUpdateView, login_view

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('my_profile/<slug:slug>', UserUpdateView.as_view(), name='my_profile'),
    path('login/', login_view, name='login'),

    
]

app_name = 'users'
