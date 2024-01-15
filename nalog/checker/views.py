from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    # post_list = Post.objects.all()
    # page_obj = get_pages(request, post_list, POSTS_STR)

    context = {
        # "page_obj": page_obj,
    }
    return render(request, "checker/index.html", context)


def download(request: HttpRequest) -> HttpResponse:
    pass
