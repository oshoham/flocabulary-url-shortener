from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import ensure_csrf_cookie
import json
import urlparse

from .models import Url


@ensure_csrf_cookie
def index(request):
    return render(request, 'url_shortener/index.html')


def shorten(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])

    body = json.loads(request.body)
    long_url = body.get('long_url')
    if not long_url:
        return HttpResponseBadRequest('Missing key in JSON: long_url')

    url, _ = Url.objects.get_or_create(url=long_url)
    data = {
        'short_url': '/'.join([request.META['HTTP_HOST'], url.short_id]),
        'long_url': url.url
    }
    return HttpResponse(json.dumps(data), content_type='application/json')


def redirect_short_url(request, short_url):
    pk = Url.decode_short_id(short_url)
    url = get_object_or_404(Url, pk=pk)
    redirect_url = url.url

    # ensure that redirect_url is always an absolute url
    if not urlparse.urlparse(redirect_url).netloc:
        redirect_url = 'http://' + redirect_url

    return redirect(redirect_url)
