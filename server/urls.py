from django.contrib import admin
from django.urls import path
from core.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('results/',recommendation),
    path('json/',json_data),
    path('hotspot/',hotspot),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
