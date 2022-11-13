import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class First_Test(unittest.TestCase):

    def test_zero_money_save(self) -> None:
        """Проверка на выгоду равную нулю"""

        service = Service("./chromedriver")
        driver = webdriver.Chrome(service=service)
        driver.get("https://copenhagencard.com/attractions")

        first_screen = driver.find_element(By.CLASS_NAME, "coi-banner__accept")
        first_screen.click()

        like_press = driver.find_element(By.CLASS_NAME, "attractions__favourite-heart")
        like_press.click()

        calc_button_click_1 = driver.find_element(By.ID, "calculator-step-1-button")
        calc_button_click_1.click()

        calc_button_click_2 = driver.find_element(By.ID, 'calculator-step-2-button')
        calc_button_click_2.click()

        calc_button_click_3 = driver.find_element(By.ID, 'calculator-step-3-button')
        calc_button_click_3.click()

        self.assertTrue("0 EUR" in driver.page_source)
        driver.quit()



