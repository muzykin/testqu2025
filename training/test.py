import unittest
import time
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

chromedriver_autoinstaller.install()

class TestWikipedia(unittest.TestCase):
    def test_open_wikipedia(self):
        driver = webdriver.Chrome()
        driver.get("https://www.wikipedia.org/")
        
        self.assertIn("Wikipedia", driver.title)

        search_box = driver.find_element(By.NAME, "search")
        search_box.clear()
        search_box.send_keys("Selenium (software)")
        search_box.send_keys(Keys.RETURN)

        time.sleep(3)

        self.assertIn("Selenium", driver.title)

        driver.save_screenshot("wikipedia_search.png")

        driver.quit()

if __name__ == "__main__":
    unittest.main()
