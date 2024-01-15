import os
from http import HTTPStatus

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    if request.method == "POST" and request.FILES:
        file = request.FILES["myfile1"]
        fs = FileSystemStorage()
        filename = fs.save("edite.xlsx", file)
        file_url = fs.url(filename)
        return render(request, "checker/index.html", {"file_url": file_url})
    return render(request, "checker/index.html")


def download(request: HttpRequest) -> HttpResponse:
    data = open(f"{settings.MEDIA_ROOT}/edite.xlsx", "rb").read()
    response = HttpResponse(
        data, content_type="application/vnd.ms-excel", status=HTTPStatus.OK
    )
    response["Content-Disposition"] = 'attachment; filename="edite.xlsx"'
    os.remove(f"{settings.MEDIA_ROOT}/edite.xlsx")
    return response
