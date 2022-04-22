from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, LikeAPIView


app_name = "api"

router = DefaultRouter()
router.register("", PostViewSet, basename="post")


urlpatterns = router.urls
urlpatterns += [
    path('like/<int:pk>/', LikeAPIView.as_view(), name='like')
]

