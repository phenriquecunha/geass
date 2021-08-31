from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import RegisterCreateView

app_name = "attendance"

urlpatterns = [
    path('register_form/', RegisterCreateView.as_view(), name='register_form')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
