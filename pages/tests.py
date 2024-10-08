from django.test import SimpleTestCase
from django.urls import reverse, resolve

from .views import HomePageView, AboutPageView


class HomepageTests(SimpleTestCase):
    def setUp(self):
        url = reverse('pages:home')
        self.response = self.client.get(url)

    def test_url_exist_at_correct_location(self):

        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
    
        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, 'home page')

    def test_homepahe_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'hi there, I should not be on the page')

    def test_homepage_url_resolves_homepageview(self):
        view = resolve('/')
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)

class AboutPage(SimpleTestCase):
    def setUp(self):
        url = reverse('pages:about')
        self.response = self.client.get(url)
    
    def test_aboutpage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_aboutpage_template(self):
        self.assertTemplateUsed(self.response, 'about.html')

    def test_aboutpage_contains_corret_html(self):
        self.assertContains(self.response, 'About Page')

    def test_aboutpage_does_not_contains_incorrect_html(self):
        self.assertNotContains(self.response, 'hi there, I should be on the page')

    def test_aboutpage_url_resolves_aboutpage(self):
        view = resolve('/about/')
        self.assertEqual(view.func.__name__, AboutPageView.as_view().__name__)
        



