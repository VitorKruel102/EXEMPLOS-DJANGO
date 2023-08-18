from django.test import TestCase
from django.urls import reverse


class Exemplo12UrlsTestCase(TestCase):


    def test_home_url_esta_correta(self):
        url = reverse('exemplo12:home')

        self.assertEqual(url, '/')