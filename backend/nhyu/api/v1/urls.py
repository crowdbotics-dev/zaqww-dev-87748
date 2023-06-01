
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Sweer23ViewSet
router = DefaultRouter()
router.register('sweer23', Sweer23ViewSet )

urlpatterns = [
    path("", include(router.urls)),
]
