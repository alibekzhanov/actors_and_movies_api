from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ActorViewSet, MovieViewSet

router = DefaultRouter()
router.register(r'actors', ActorViewSet)
router.register(r'movies', MovieViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
