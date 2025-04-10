"Test for https://the-internet.herokuapp.com/broken_images"
import unittest

import requests
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


class BrokenImages(unittest.TestCase):
    def setUp(self):
        self.baseurl = "https://the-internet.herokuapp.com/"
        self.url = f"{self.baseurl}broken_images"
        self.driver = webdriver.Chrome()

    def test_broken_images(self):
        "visit URL, get screenshot, assest broken images"
        driver = self.driver
        res = driver.get(self.url)
        self.assertIn('The Internet', driver.title)      

        image1 = driver.find_element(By.CSS_SELECTOR, "#content > div > img:nth-child(2)")
        image2 = driver.find_element(By.CSS_SELECTOR, "#content > div > img:nth-child(3)")
        image3 = driver.find_element(By.CSS_SELECTOR, "#content > div > img:nth-child(4)")
        image1_url = "https://the-internet.herokuapp.com/asdf.jpg"
        image2_url = "https://the-internet.herokuapp.com/hjkl.jpg"
        image3_url = "https://the-internet.herokuapp.com/img/avatar-blank.jpg"
        image1_result = requests.get(image1_url)
        self.assertEqual(image1_result.status_code, 404)
        image2_result = requests.get(image2_url)
        self.assertEqual(image2_result.status_code, 404)
        image3_result = requests.get(image3_url)
        self.assertEqual(image3_result.status_code, 200)
        content = driver.find_element(By.ID, "content")
        driver.save_screenshot("broken_images.png")
        self.assertEqual(content.text, "Broken Images")


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()