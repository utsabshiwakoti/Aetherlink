from django.test import TestCase

# Create your tests here.

class HomePageTest(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_page_contains_correct_html(self):
        response = self.client.get('/')
        self.assertContains(response, 'Homepage')

    def test_home_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/')
        self.assertNotContains(
            response, 'Hi there! I should not be on the page.')

    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_contains_correct_html(self):
        response = self.client.get('/about/')
        self.assertContains(response, 'About Page')

    def test_about_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/about/')
        self.assertNotContains(
            response, 'Hi there! I should not be on the page.')

    def test_contact_page_status_code(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)

    def test_contact_page_contains_correct_html(self):
        response = self.client.get('/contact/')
        self.assertContains(response, 'Contact Page')

    def test_contact_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/contact/')
        self.assertNotContains(
            response, 'Hi there! I should not be on the page.')