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
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post_create/', PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('', HomePageView.as_view(), name='home'),
    path('<int:post_id>/<int:user_preference>/', like_dislike, name='like_dislike'),
    path('<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
    
]

app_name = 'posts'

