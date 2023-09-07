"""
URL configuration for hngx project.

"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("hngx.urls")),

    # Docs
    #path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    #path("api-docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
] 