from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class Exemplo10UrlsTestCase(TestCase):


    def test_url_home_esta_correta(self):
        url = reverse('exemplo10:home')

        self.assertEqual(url, '/')