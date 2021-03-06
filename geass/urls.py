from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # django admin
    path('admin/', admin.site.urls),

    # user management
    path('accounts/', include('allauth.urls')),

    # local
    path('', include('pages.urls')),
    path('scheduling/', include('scheduling.urls')),
    path('attendance/', include('attendance.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)