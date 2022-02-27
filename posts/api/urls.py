from .views import PostList
from rest_framework.routers import DefaultRouter


app_name = 'api'

router = DefaultRouter()
router.register('', PostList, basename='post')


urlpatterns = router.urls
