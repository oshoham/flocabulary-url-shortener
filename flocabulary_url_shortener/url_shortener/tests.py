from django.test import TestCase
from django.core.urlresolvers import reverse

from .models import Url


class RedirectShortUrlViewTests(TestCase):
    def test_responds_with_404_when_short_url_does_not_exist(self):
        response = self.client.get(reverse('redirect_short_url', args=['AbCDe']))
        self.assertEqual(response.status_code, 404)

    def test_redirects_when_short_url_exists(self):
        url = Url.objects.create(url='www.example.com')
        response = self.client.get(reverse('redirect_short_url', args=[url.short_id]))
        self.assertRedirects(response, url.url, fetch_redirect_response=False)
