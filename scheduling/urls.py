from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import DetourCreateView, DetourListView, DetourDetailView, DetourUpdateView, DetourDeleteView

app_name = "scheduling"

urlpatterns = [
    path('detour_list/', DetourListView.as_view(), name='detour_list'),
    path('detour_form/', DetourCreateView.as_view(), name="detour_form"),
    path('detour_detail/?P<pk>\d+/', DetourDetailView.as_view(), name='detour_detail'),
    path('detour_update/?P<pk>\d+/', DetourUpdateView.as_view(), name='detour_update'),
    path('detour_delete/?P<pk>\d+/', DetourDeleteView.as_view(), name='detour_list'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        documment_root=settings.MEDIA_ROOT,
    )