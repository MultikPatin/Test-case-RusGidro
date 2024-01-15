from django.urls import path

from checker import views

app_name = "checker"

urlpatterns = [
    path("", views.index, name="index"),
    path("download/", views.download, name="download"),
]
