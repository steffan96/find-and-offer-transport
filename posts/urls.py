from django.urls import path

#from posts.forms import OfferingCreationForm
from .views import (
    PostDetailView,  
    PostUpdateView, 
    PostDeleteView, 
    HomePageView,
    like_dislike,
    AddCommentView,
    PostCreateView,
    )


urlpatterns = [
    path('<slug:slug>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('<slug:slug>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post_create/', PostCreateView.as_view(), name='post_create'),
    path('<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('', HomePageView.as_view(), name='home'),
    path('<int:post_id>/<int:user_preference>/', like_dislike, name='like_dislike'),
    path('comment/<int:pk>/', AddCommentView.as_view(), name='add_comment'),
    
]

app_name = 'posts'

