from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from core.views import rpgclassViewSet, rpgraceViewSet, itensViewSet, skillsViewSet, characterViewSet
from media.router import router as media_router

router = DefaultRouter()
router.register(r'class', rpgclassViewSet)
router.register(r'race', rpgraceViewSet)
router.register(r'itens', itensViewSet)
router.register(r'skills', skillsViewSet)
router.register(r'characters', characterViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/media/", include(media_router.urls)),
]
urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)