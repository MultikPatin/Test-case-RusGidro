from http import HTTPStatus

from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from checker import services
from checker.exeptions import NotXLSXFile

file_storage = FileSystemStorage()
report_service = services.Report(file_storage=file_storage)


def index(request: HttpRequest) -> HttpResponse:
    file_name = None
    if request.method == "POST" and request.FILES:
        file = request.FILES["file_to_check"]
        try:
            file_name = report_service.save_file(file)
            report_service.generate_report(file_name)
        except NotXLSXFile as e:
            messages.error(request, e.error_message)

        context = {"file_url": file_name, "errors": None}

        return render(request, "checker/index.html", context)
    return render(request, "checker/index.html")


def download(request: HttpRequest) -> HttpResponse:
    file_path = report_service.get_report_file_path()
    file = open(file_path, "rb").read()
    response = HttpResponse(
        file, content_type="application/vnd.ms-excel", status=HTTPStatus.OK
    )
    response["Content-Disposition"] = 'attachment; filename="report.xlsx"'
    return response
