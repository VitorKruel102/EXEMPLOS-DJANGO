from django.test import TestCase
from django.urls import resolve, reverse

from app_exemplo07 import views

class AppExemplo07HomeViewsTestCase(TestCase):


    def test_retorna_view_correta(self):
        url = reverse("exemplo07:home")
        view = resolve(url)
        
        self.assertEqual(views.home, view.func)

    def test_status_200_da_view(self):
        url = reverse('exemplo07:home')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_retorna_template_correto(self):
        url = reverse('exemplo07:home')
        response = self.client.get(url)

        self.assertTemplateUsed(response, 'app_exemplo07/pages/home.html')

    def test_retorno_context_exemplo(self):
        url = reverse('exemplo07:home')
        response = self.client.get(url)

        self.assertEqual(response.context['exemplo'], 1)