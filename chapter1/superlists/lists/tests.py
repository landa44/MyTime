from django.test import TestCase
from .views import *
from django.urls import resolve
from django.http import HttpRequest

class HomePageTest(TestCase):
  def test_root_url_resolves_to_home_page_views(self):
    found = resolve('/')
    self.assertEqual(found.func, home_page)

  def test_home_page_returns_correct_html(self):
    response = self.client.get('/')
    self.assertTemplateUsed(response, 'home.html')