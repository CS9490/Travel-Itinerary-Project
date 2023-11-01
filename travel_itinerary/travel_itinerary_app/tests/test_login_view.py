from django.test import TestCase
from django.urls import reverse

class LoginUnitTest(TestCase):

    def test_login_with_empty_credentials(self):
        response = self.client.post(reverse('login'), {'username': '', 'password': ''})
        self.assertContains(response, "This field is required.")

    def test_login_view_status_code(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_login_view_uses_correct_template(self):
        response = self.client.get(reverse('login'))
        self.assertTemplateUsed(response, 'travel_itinerary_app/login.html')
