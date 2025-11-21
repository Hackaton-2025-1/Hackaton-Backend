from django.contrib import admin
from django.urls import include, path
from core.views.colecoes import ColecoesViewSet
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.routers import DefaultRouter

from core.views import UserViewSet

from core.views import ColecoesViewSet, CategoriasViewSet, ArtefatosViewSet


router = DefaultRouter()

router.register(r'usuarios', UserViewSet, basename='usuarios')

router.register(r"colecoes", ColecoesViewSet)
router.register(r"categorias", CategoriasViewSet)
router.register(r"artefatos", ArtefatosViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # OpenAPI 3
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'api/swagger/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui',
    ),
    path(
        'api/redoc/',
        SpectacularRedocView.as_view(url_name='schema'),
        name='redoc',
    ),
    # API
    path('api/', include(router.urls)),
]
