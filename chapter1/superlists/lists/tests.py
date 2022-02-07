from django.test import TestCase
from .views import *
from django.urls import resolve

class HomePageTest(TestCase):
  def test_root_url_resolves_to_home_page_views(self):
    found = resolve('/')
    self.assertEqual(found.func, home_page)