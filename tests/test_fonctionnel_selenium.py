import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_fonctionnel_page_acceuil(self):
        driver = self.driver
        driver.get("http://127.0.0.1:5001")
        elem = driver.find_element(By.ID, "length-btn")
        elem = driver.find_element(By.ID, "weight-btn")
        elem = driver.find_element(By.ID, "temperature-btn")
        self.assertIn("Unit Converter", driver.title)
        self.assertNotIn("No results found.", driver.page_source)
        print('page url: '+ driver.current_url)
        print('page title: '+ driver.title)

    def test_fonctionnel_page_length(self):
        driver = self.driver
        driver.get("http://127.0.0.1:5001/length")
        select = Select(driver.find_element(By.NAME, "from_unit"))
        select.select_by_value("m")
        select = Select(driver.find_element(By.NAME, "to_unit"))
        select.select_by_value("km")
        element = driver.find_element(By.NAME, "value")
        element.send_keys(1000)
        driver.find_element(By.ID, "submit").click()
        time.sleep(5)
        contents = driver.find_elements(By.CLASS_NAME, 'result-output')
        print('page url: '+ driver.current_url)
        for content in contents:
            print('Result of your calculation: '+ content.text)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()