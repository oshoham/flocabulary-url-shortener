from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^shorten$', views.shorten, name='shorten'),
    url(r'^(?P<short_url>[0-9a-zA-Z]+)$', views.redirect_short_url, name='redirect_short_url')
]
