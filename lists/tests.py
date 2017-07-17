from django.urls import resolve
from django.test import TestCase
from lists.views import home_page
from django.http import HttpRequest



# Create your tests here.
class HomePageTest(TestCase):
    def test_root_rul_resolves_to_home_page_view(self):
        #check that resolve when called with the root of the site, finds homepage function
        found = resolve ('/')
        #returns the html we want.
        self.assertEqual(found.func, home_page)
    def test_home_page_returns_correct_html(self):
        #create HttpRequest object
        request = HttpRequest()
        #pass HttpRequest to homepage
        response = home_page(request)
        #extract .content and use .decode() to convert them to a html string
        html=response.content.decode('utf8')
        #test if starts with <html>
        self.assertTrue(html.startswith('<html>'))
        #tests that there is a title section with the words to-do list.
        self.assertIn('<title>To-Do lists</title>', html)
        #tests that it ends with </html>
        self.assertTrue(html.endswith('</html>'))
