from django.test import TestCase

class VaccinationTests(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_page_should_render_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'vaccination/homepage.html')

    def test_ping_returns_pong(self):
        response = self.client.get('/ping/')
        self.assertEqual(response.content, b'pong')