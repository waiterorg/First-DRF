from django.urls import include, path
from rest_framework import routers
from .views import ArticleViewSet, UserViewSet, AuthorRetrieve

app_name = "api"

router = routers.SimpleRouter()
router.register('articles', ArticleViewSet, basename="articles")
router.register('users', UserViewSet, basename="users")

urlpatterns = [
    path('', include(router.urls)),
    path('authors/<int:pk>/', AuthorRetrieve.as_view(), name="authors_detail"),
]
