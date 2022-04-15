from .views import PostViewSet
from rest_framework.routers import DefaultRouter


app_name = 'api'

router = DefaultRouter()
router.register('', PostViewSet, basename='post')


urlpatterns = router.urls
