import time
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.keys import Keys

class SignUpEndToEndTest(StaticLiveServerTestCase):
    def setUp(self):
        # Initialize the Selenium WebDriver (you may need to specify the path to your WebDriver)
        self.driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

    def tearDown(self):
        # Close the WebDriver when the test is finished
        self.driver.close()

    def test_signup(self):
        # Open the sign-up page
        self.driver.get(self.live_server_url + '/signup/')

        # Fill out the sign-up form with test data
        self.driver.find_element_by_id('id_username').send_keys('testuser')
        self.driver.find_element_by_id('id_email').send_keys('testuser@example.com')
        self.driver.find_element_by_id('id_password1').send_keys('testpassword123')
        self.driver.find_element_by_id('id_password2').send_keys('testpassword123')

        # Submit the form
        self.driver.find_element_by_xpath('//button[text()="Sign Up"]').click()

        # Wait for a few seconds (you can use WebDriverWait for better synchronization)
        time.sleep(2)

        # Check if the user is redirected to the home page upon successful sign-up
        self.assertEqual(self.driver.current_url, self.live_server_url + '/home/')

    def test_invalid_signup(self):
        # Open the sign-up page
        self.driver.get(self.live_server_url + '/signup/')

        # Fill out the sign-up form with invalid data
        self.driver.find_element_by_id('id_username').send_keys('testuser')
        self.driver.find_element_by_id('id_email').send_keys('invalidemail')  # Invalid email format
        self.driver.find_element_by_id('id_password1').send_keys('testpassword123')
        self.driver.find_element_by_id('id_password2').send_keys('differentpassword')

        # Submit the form
        self.driver.find_element_by_xpath('//button[text()="Sign Up"]').click()

        # Wait for a few seconds (you can use WebDriverWait for better synchronization)
        time.sleep(2)

        # Check if the sign-up form is redisplayed with errors
        self.assertEqual(self.driver.current_url, self.live_server_url + '/signup/')
        self.assertIn('errorlist', self.driver.page_source)  # Check for the presence of error messages

if __name__ == '__main__':
    import unittest
    unittest.main()
