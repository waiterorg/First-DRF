from django.urls import include, path
from rest_framework import routers
from .views import ArticleViewSet, UserViewSet

app_name = "api"

router = routers.SimpleRouter()
router.register('articles', ArticleViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
