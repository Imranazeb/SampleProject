from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static


urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    # path("__reload__/", include("django_browser_reload.urls")),
    
    path('', include('common.core.urls')),
    path('userauths/', include('common.userauths.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)