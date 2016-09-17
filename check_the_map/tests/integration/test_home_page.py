from django.test import TestCase


class HomePageTestCase(TestCase):
    def setUp(self):
        pass

    def test_home_page(self):
        """Basic test to ensure homepage loads without an error"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)