from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name = "attendance"

urlpatterns = [
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
