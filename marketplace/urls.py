from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin  # type: ignore
from django.urls import path, include  # type: ignore

urlpatterns = [
    path("", include("core.urls")),
    path("dashboard/", include("dashboard.urls")),
    path("items/", include("item.urls")),
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
