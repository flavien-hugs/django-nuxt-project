# backend.urls.py

from django.contrib import admin
from django.urls import path, include

from core.routers import router
from rest_framework_simplejwt.views import(
    TokenObtainPairView, TokenRefreshView,
    TokenVerifyView
)

token_obtain = TokenObtainPairView.as_view()
token_refresh = TokenRefreshView.as_view()
verify_token = TokenVerifyView.as_view()


urlpatterns = [
    path('admin/', admin.site.urls),

    path("api/", include(router.urls)),
    path('api/auth/', include(
        'rest_framework.urls')
    ),
    path(route="api/token/obtain/",
        view=token_obtain,
        name="obtain_token"
    ),
    path(route='api/token/verify/',
        view=verify_token,
        name='token_verify'
    ),
    path(route="api/token/refresh/",
        view=token_refresh,
        name="refresh_token"
    ),
]
