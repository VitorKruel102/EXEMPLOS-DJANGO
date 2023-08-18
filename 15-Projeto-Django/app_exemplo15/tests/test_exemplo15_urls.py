from django.test import TestCase
from django.urls import reverse


class Exemplo15UrlsTestCase(TestCase):


    def test_home_urls_esta_correta(self):
        url = reverse('exemplo15:home')

        self.assertAlmostEqual(url, '/')

