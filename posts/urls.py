from django.urls import path

#from posts.forms import OfferingCreationForm
from .views import (
    PostDetailView, 
    OfferingCreateView, 
    PostUpdateView, 
    PostDeleteView, 
    LookingCreateView, 
    HomePageView,
    like_dislike,)


urlpatterns = [
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('offering_new/', OfferingCreateView.as_view(), name='offering_new'),
    path('looking_new/', LookingCreateView.as_view(), name='looking_new'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('', HomePageView.as_view(), name='home'),
    path('<int:post_id>/<int:user_preference>/', like_dislike, name='like_dislike')
]

app_name = 'posts'