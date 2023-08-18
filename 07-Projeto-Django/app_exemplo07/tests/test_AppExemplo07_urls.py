from django.test import TestCase
from django.urls import reverse


class   AppExemplo07UrlsTestCase(TestCase):
    
    
    def test_retorno_da_url_esta_correta(self):
        url = reverse('exemplo07:home')
        self.assertEqual(url, '/')
