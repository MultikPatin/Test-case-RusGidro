from http import HTTPStatus

import services
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    if request.method == "POST" and request.FILES:
        file = request.FILES["myfile1"]
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)

        report_service = services.Report(settings.MEDIA_ROOT, filename)
        report_service.save_report()

        return render(request, "checker/index.html", {"file_url": filename})
    return render(request, "checker/index.html")


def download(request: HttpRequest) -> HttpResponse:
    data = open(f"{settings.MEDIA_ROOT}/report.xlsx", "rb").read()
    response = HttpResponse(
        data, content_type="application/vnd.ms-excel", status=HTTPStatus.OK
    )
    response["Content-Disposition"] = 'attachment; filename="report.xlsx"'
    return response
