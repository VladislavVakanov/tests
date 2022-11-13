import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class Second_Test(unittest.TestCase):
    def test_more_than_zero_save(self) -> None:
        """Проверка на выгоду больше нуля"""

        service = Service("./chromedriver")
        driver = webdriver.Chrome(service=service)
        driver.get("https://copenhagencard.com/attractions")

        first_screen = driver.find_element(By.CLASS_NAME, "coi-banner__accept")
        first_screen.click()

        like_press_1 = driver.find_element(By.XPATH,
                                           '//*[@id="block-views-block-attractions-block-1"]/div/div/div[2]/div/div[2]/div[5]/span')
        like_press_1.click()

        like_press_2 = driver.find_element(By.XPATH,
                                           '//*[@id="block-views-block-attractions-block-1"]/div/div/div[2]/div/div[2]/div[6]/span')
        like_press_2.click()

        like_press_3 = driver.find_element(By.XPATH,
                                           '//*[@id="block-views-block-attractions-block-1"]/div/div/div[2]/div/div[2]/div[7]/span')
        like_press_3.click()

        calc_button_click_1 = driver.find_element(By.ID, "calculator-step-1-button")
        calc_button_click_1.click()

        calc_button_click_2 = driver.find_element(By.ID, 'calculator-step-2-button')
        calc_button_click_2.click()

        calc_button_click_3 = driver.find_element(By.ID, 'calculator-step-3-button')
        calc_button_click_3.click()

        not self.assertTrue("0 EUR" in driver.page_source)
        driver.quit()