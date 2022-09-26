"""fastrpg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from media.router import router as media_router




from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from core.views import rpgclassViewSet, rpgraceViewSet, itensViewSet, skillsViewSet, characterViewSet

router = DefaultRouter()
router.register(r'class', rpgclassViewSet)
router.register(r'race', rpgraceViewSet)
router.register(r'itens', itensViewSet)
router.register(r'skills', skillsViewSet)
router.register(r'characters', characterViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path("api/media/", include(media_router.urls)),
]
urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)