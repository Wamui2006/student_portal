from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),        # built-in admin site
    path("", include("dashboard.urls")),    # include dashboard app’s URL patterns
]
