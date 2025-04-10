"Test for https://the-internet.herokuapp.com/broken_images"
import unittest
import requests
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class BrokenImages(unittest.TestCase):
    def setUp(self):
        self.baseurl = "https://the-internet.herokuapp.com/"
        self.url = f"{self.baseurl}broken_images"
        self.driver = webdriver.Chrome()

    def test_broken_images(self):
        "Visit URL, get screenshot, assert broken images"
        driver = self.driver
        try:
            driver.get(self.url)
            self.assertIn('The Internet', driver.title)

            try:
                image1 = driver.find_element(By.CSS_SELECTOR, "#content > div > img:nth-child(2)")
                image2 = driver.find_element(By.CSS_SELECTOR, "#content > div > img:nth-child(3)")
                image3 = driver.find_element(By.CSS_SELECTOR, "#content > div > img:nth-child(4)")
            except NoSuchElementException as e:
                self.fail(f"Image not found: {e}")

            image1_url = image1.get_attribute("src")
            image2_url = image2.get_attribute("src")
            image3_url = image3.get_attribute("src")

            image1_result = requests.get(image1_url, timeout=5)
            self.assertEqual(image1_result.status_code, 404)
            image2_result = requests.get(image2_url, timeout=5)
            self.assertEqual(image2_result.status_code, 404)
            image3_result = requests.get(image3_url, timeout=5)
            self.assertEqual(image3_result.status_code, 200)

            content = driver.find_element(By.ID, "content")
            driver.save_screenshot("brokenimages.png")
            print(f"Captured screenshot: brokenimages.png")
            self.assertIn("Broken Images", content.text.strip())
        finally:
            driver.quit()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()