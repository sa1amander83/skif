from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.skif.urls')),
    path('api/', include('apps.skif_api.urls')),
    path('', include('apps.registration.urls')),
    path('', include('apps.accounts.urls')),
    path('', include('apps.dialogs.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
