from django.contrib import admin
from django.urls import path,include
from rest_framework.documentation import include_docs_urls

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('apps.products.urls')),
    path('users/', include('apps.users.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("api/v1/docs/", include_docs_urls(title = "Zebrands Backend users")),    
]