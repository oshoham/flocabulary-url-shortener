from django.http import HttpResponse, Http404
from django.shortcuts import redirect, get_object_or_404

from .models import Url


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def redirect_short_url(request, short_url):
    pk = Url.decode_short_id(short_url)
    url = get_object_or_404(Url, pk=pk)
    return redirect(url.url)
