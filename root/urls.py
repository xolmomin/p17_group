from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from root import settings
from apps.event_admin import event_admin_site

urlpatterns = [
    path("admin/", admin.site.urls),
    path("event-admin/", event_admin_site.urls),
    path('', include('apps.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# static va media nginx
