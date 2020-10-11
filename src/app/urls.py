from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from ambitos.urls import ambitos_patterns
from caracteristicas.urls import caracteristicas_patterns


urlpatterns = [
    path('admin/', admin.site.urls),
    # PATH de AUTH
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),
    # PATH APPS
    path('', include('core.urls')),
    path('ambitos/', include(ambitos_patterns)),
    path('caracteristicas/', include(caracteristicas_patterns)),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
        )
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
        )
