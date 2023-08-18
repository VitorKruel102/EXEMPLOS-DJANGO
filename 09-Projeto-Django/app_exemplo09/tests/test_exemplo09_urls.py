from unittest import TestCase
from django.urls import reverse

# Create your tests here.
class Exemplo09UrlsTestCase(TestCase):


    def test_se_urls_esta_correta(self):
        url = reverse('exemplo09:home')

        self.assertEqual(url, '/')