from django.test import TestCase
from django.core.urlresolvers import reverse
import json

from .models import Url


class RedirectShortUrlViewTests(TestCase):
    def test_responds_with_404_when_short_url_does_not_exist(self):
        response = self.client.get(reverse('redirect_short_url', args=['AbCDe']))
        self.assertEqual(response.status_code, 404)

    def test_redirects_properly_when_long_url_is_a_relative_url(self):
        url = Url.objects.create(url='www.example.com')
        response = self.client.get(reverse('redirect_short_url', args=[url.short_id]))
        self.assertRedirects(response, 'http://www.example.com', fetch_redirect_response=False)

    def test_redirects_properly_when_long_url_is_an_absolute_url(self):
        url = Url.objects.create(url='http://www.example.com')
        response = self.client.get(reverse('redirect_short_url', args=[url.short_id]))
        self.assertRedirects(response, 'http://www.example.com', fetch_redirect_response=False)


class ShortenViewTests(TestCase):
    def setUp(self):
        self.http_host = 'urlshortener.com'

    def test_creates_short_url_when_long_url_is_new(self):
        long_url = 'foo.bar.com'
        data = json.dumps({'long_url': long_url})
        response = self.client.post(reverse('shorten'), data=data, content_type='application/json', HTTP_HOST=self.http_host)
        url = Url.objects.get(url=long_url)

        self.assertTrue(url)
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {
            u'short_url': unicode(self.http_host + '/' + url.short_id),
            u'long_url': unicode(long_url)
        })

    def test_responds_with_existing_short_url_when_long_url_exists(self):
        long_url = 'a.fake.link'
        url = Url.objects.create(url=long_url)
        data = json.dumps({'long_url': long_url})
        response = self.client.post(reverse('shorten'), data=data, content_type='application/json', HTTP_HOST=self.http_host)

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {
            u'short_url': unicode(self.http_host + '/' + url.short_id),
            u'long_url': unicode(long_url)
        })

    def test_responds_with_405_when_method_is_not_post(self):
        response = self.client.get(reverse('shorten'))
        self.assertEqual(response.status_code, 405)
