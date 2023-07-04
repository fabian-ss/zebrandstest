from django.urls import path, include
from .api import UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'', UserViewSet, 'users')

urlpatterns = [
    path("api/v1/", include(router.urls)),
]

