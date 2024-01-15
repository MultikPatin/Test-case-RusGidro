from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("checker.urls", namespace="checker")),
    path("admin/", admin.site.urls),
]

handler404 = "core.views.page_not_found"
handler403 = "core.views.csrf_failure"
