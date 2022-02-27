"""findoffer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls



from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', include('chat.urls', namespace='chat')),
    path('posts/', include('posts.urls', namespace='posts')),
    path('users/', include('django.contrib.auth.urls')),
    path('users/', include('accounts.urls', namespace='accounts')),
    path('social/', include('social_django.urls', namespace='social')),
    path('api/', include('posts.api.urls', namespace='api')),
    path('api/users/', include('accounts.api.urls', namespace='api_users')),
    path('docs/', include_docs_urls(title='FindOffer')),
    path('schema', get_schema_view(
        title="FindOffer",
        description="API for the FindOffer site",
        version="1.0.0"
    ), name='FindOfferAPI-schema'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
