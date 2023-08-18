from django.test import TestCase
from django.urls import reverse


class Exemplo18UrlsTestCase(TestCase):

    def test_home_url_esta_correta(self):
        url = reverse('exemplo18:home')

        self.assertEqual(url, '/')
    