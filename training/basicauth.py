import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

SUCCESS_ELEMENT = (By.TAG_NAME, "p")

class TestBasicAuthLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def test_correct_credentials(self):
        username, password = "admin", "admin"
        url = f"https://{username}:{password}@the-internet.herokuapp.com/basic_auth"
        self.driver.get(url)
        time.sleep(2)
        
        try:
            message = self.driver.find_element(*SUCCESS_ELEMENT).text
        except:
            message = "Not authorized"
        
        print(f"Captured message: {message}")
        self.assertIn("Congratulations!", message)
        
    def test_incorrect_credentials(self):
        username, password = "admin1", "admin"
        url = f"https://{username}:{password}@the-internet.herokuapp.com/basic_auth"
        self.driver.get(url)
        time.sleep(2)
        
        try:
            message = self.driver.find_element(*SUCCESS_ELEMENT).text
        except:
            message = "Not authorized"
        
        print(f"Captured message: {message}")
        self.assertIn("Not authorized", message)
        
    def test_empty_credentials(self):
        username, password = "", ""
        url = f"https://{username}:{password}@the-internet.herokuapp.com/basic_auth"
        self.driver.get(url)
        time.sleep(2)
        
        try:
            message = self.driver.find_element(*SUCCESS_ELEMENT).text
        except:
            message = "Not authorized"
        
        print(f"Captured message: {message}")
        self.assertIn("Not authorized", message)
        
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
