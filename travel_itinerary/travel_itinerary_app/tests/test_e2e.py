from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.contrib.auth.models import User
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

class UserLoginLogoutTests(StaticLiveServerTestCase):

    def setUp(self):
        # Setup the Firefox 
        self.browser = webdriver.Firefox()
        self.user = User.objects.create_user(username='testing', password='RightPassword')

    def tearDown(self):
        #closing the browser after each test
        self.browser.quit()

    def test_user_can_login_and_logout(self):
        # homepage
        self.browser.get(self.live_server_url)
        
        # Waiting page to load 
        wait = WebDriverWait(self.browser, 10)
        

        try:
            # we login here
            sign_in_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'Login')))
            sign_in_link.click()
            
        except TimeoutException:
            print("Login not found")

      
        username_input = self.browser.find_element(By.NAME, 'username')
        password_input = self.browser.find_element(By.NAME, 'password')

        # entering username and password 
        username_input.send_keys('testing')
        password_input.send_keys('RightPassword')
        password_input.send_keys(Keys.RETURN)

        

    
        wait.until_not(EC.presence_of_element_located((By.LINK_TEXT, 'Login')))
        wait.until_not(EC.presence_of_element_located((By.LINK_TEXT, 'Sign Up')))

        
        #logout too quick, just for testing purpose 
        time.sleep(3)
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Logout'))).click()

        
        self.assertTrue(wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'Login'))))
        
