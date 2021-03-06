"""api_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from main.views import CategoryViewSet, PostViewSet,CommentViewSet, RatingViewSet, LikeAPIView, \
    HistoryAPIView

from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.routers import DefaultRouter


schema_view = get_schema_view(
    openapi.Info(
        title='Stack API',
        default_version='v1',
        description='Test Description',
        contact=openapi.Contact(email='saralicei1@gmail.com'),
    ),
    public=True,
)


router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('comments', CommentViewSet)
router.register('categories', CategoryViewSet)
router.register('rating', RatingViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/docs/', schema_view.with_ui()),
    path('v1/api/auth/', include('rest_framework_social_oauth2.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('v1/api/like/<int:post_id>/', LikeAPIView.as_view()),
    path('v1/api/history/', HistoryAPIView.as_view()),
    path('v1/api/account/', include('account.urls')),
    path('v1/api/', include(router.urls)),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)


