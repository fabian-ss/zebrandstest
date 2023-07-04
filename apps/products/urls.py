from django.urls import path, include
from .api import ProductViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'', ProductViewSet, 'products')

urlpatterns = [
    path("api/v1/", include(router.urls)),
]

