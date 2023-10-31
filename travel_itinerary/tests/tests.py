
from travel_itinerary.travel_itinerary_app.itinerary import Itinerary  # Import the Itinerary class
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User  # Import User model for user creation


#unit test
class ItineraryTestCase(TestCase):
    def setUp(self):
        # Create an instance of the Itinerary class
        self.itinerary = Itinerary()

    def test_capture_form_data(self):
        # Create a sample form data dictionary
        form_data = {
            "departure_date": "2023-01-01",
            "return_date": "2023-01-07",
            "origin": "New York",
            "destination": "Los Angeles",
            "travelers": 2,
            "min_amount": 500,
            "max_amount": 2000,
        }

        # Call the capture_form_data method with the sample form data
        self.itinerary.capture_form_data(form_data)

        # Assert that the instance variables of the Itinerary object have been set correctly
        self.assertEqual(self.itinerary.departure_date, "2023-01-01")
        self.assertEqual(self.itinerary.return_date, "2023-01-07")
        self.assertEqual(self.itinerary.origin, "New York")
        self.assertEqual(self.itinerary.destination, "Los Angeles")
        self.assertEqual(self.itinerary.travelers, 2)
        self.assertEqual(self.itinerary.min_amount, 500)
        self.assertEqual(self.itinerary.max_amount, 2000)



#Integraton Test

class LoginIntegrationTestCase(TestCase):
    def setUp(self):
        # Create a test user for login testing
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_valid_login(self):
        # Test a valid login scenario
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 302)  # Check if the user is redirected after successful login

    def test_invalid_login(self):
        # Test an invalid login scenario
        response = self.client.post(reverse('login'), {'username': 'invaliduser', 'password': 'invalidpassword'})
        self.assertEqual(response.status_code, 200)  # Check if the login form is redisplayed with errors


