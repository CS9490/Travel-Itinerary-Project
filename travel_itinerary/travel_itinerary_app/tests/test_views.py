from django.test import TestCase
from django.urls import reverse

class ViewTestCase(TestCase):
    def setUp(self):
        self.signup_url = reverse('signup')
        self.user_data = {
            'username': 'newuser',
            'email': 'newuser@example.com',  # Assuming your form requires an email
            'password1': 'testpassword123',
            'password2': 'testpassword123',
            # Include any other required fields from your SignupForm
        }
    
    def test_signup_view_get(self):
        response = self.client.get(self.signup_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'travel_itinerary_app/signup.html')
    
    def test_signup_view_post_success(self):
        response = self.client.post(self.signup_url, self.user_data)
        self.assertEqual(response.status_code, 302)  # Check for redirect after successful signup
        self.assertRedirects(response, reverse('home'))  # Assuming 'home' is the name of your homepage URL
    
    def test_signup_view_post_failure(self):
        # Modify user_data to create an invalid form submission, e.g., passwords don't match
        invalid_user_data = self.user_data.copy()
        invalid_user_data['password2'] = 'wrongpassword'
        response = self.client.post(self.signup_url, invalid_user_data)
        self.assertEqual(response.status_code, 200)  # Page reloads with form errors
        # Use the actual error message from your form's validation
        self.assertFormError(response, 'form', 'password2', ['The two password fields didn’t match.'])
