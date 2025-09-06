from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',include('landingPage.urls')),
    path("cart/", include("cart.urls")),
    path("order/", include("order.urls")),  # checkout + payments
]

if settings.DEBUG:  # serve media & static in development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
