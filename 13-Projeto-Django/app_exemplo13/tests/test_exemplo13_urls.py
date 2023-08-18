from django.test import TestCase
from django.urls import reverse


class Exemplo13UrlsTestCase(TestCase):


    def test_home_urls_esta_correta(self):
        url = reverse('exemplo13:home')

        self.assertEqual(url, '/')
