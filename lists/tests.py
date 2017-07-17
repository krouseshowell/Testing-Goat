from django.urls import resolve
from django.test import TestCase
from lists.views import home_page
HttpRequest


# Create your tests here.
class HomePageTest(TestCase):
    def test_root_rul_resolves_to_home_page_view(self):
        #check that resolve when called with the root of the site, finds homepage function
        found = resolve ('/')
        #returns the html we want.
        self.assertEqual(found.func, home_page)
