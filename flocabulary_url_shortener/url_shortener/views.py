from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render, redirect, get_object_or_404
import json

from .models import Url


def index(request):
    return render(request, 'url_shortener/index.html')


def shorten(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])

    body = json.loads(request.body)
    url, _ = Url.objects.get_or_create(url=body['long_url'])
    data = {
        'short_url': url.short_id,
        'long_url': url.url
    }
    return HttpResponse(json.dumps(data), content_type='application/json')


def redirect_short_url(request, short_url):
    pk = Url.decode_short_id(short_url)
    url = get_object_or_404(Url, pk=pk)
    return redirect(url.url)
