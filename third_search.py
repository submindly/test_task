import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time


class OrgSearch(unittest.TestCase):
    def setUp(self):
        driver_path_win = 'C:\\Python\\drivers\\chromedriver.exe'
        driver_path_nix = '/Users/submindly/Projects/webdrivers/chromedriver'
        self.driver = webdriver.Chrome(driver_path_nix)

    def test_search_in_ya(self):
        driver = self.driver
        driver.get('https://yandex.ru')
        try:
            self.assertIn('Яндекс', driver.title)
            time.sleep(2)
            self.assertTrue(driver.find_element_by_name('text'))
            driver.find_element_by_name('text').send_keys('Тензор')
            time.sleep(1)
            self.assertTrue(driver.find_element_by_xpath("//div[ancestor::div/@class='popup__content']"))
            time.sleep(1)
            driver.find_element_by_name('text').send_keys(Keys.RETURN)
            time.sleep(1)
            self.assertTrue(driver.find_element_by_xpath("//ul[ancestor::div/@class='content__left']"))
            self.assertEqual(driver.find_element_by_xpath("//a[ancestor::div/@class='organic__subtitle typo typo_type_greenurl'][1]").text, 'tensor.ru')
            time.sleep(2)
        except NoSuchElementException:
            pass  # log

        def tearDown(self):
            self.driver.close()


if __name__ == '__main__':
    unittest.main()
