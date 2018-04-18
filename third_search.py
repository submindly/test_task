import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class OrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('C:\\Python\\drivers\\chromedriver.exe')

    def test_search_in_ya(self):
        driver = self.driver
        driver.get('https://yandex.ru')
        self.assertIn('Яндекс', driver.title)
        time.sleep(2)
        search = driver.find_element_by_name('text')
        search.send_keys('Тензор')
        time.sleep(1)
        self.assertTrue(driver.find_element_by_xpath("//div[ancestor::div/@class='popup__content']"))
        time.sleep(1)
        driver.find_element_by_name('text').send_keys(Keys.RETURN)
        time.sleep(1)
        self.assertTrue(driver.find_element_by_xpath("//ul[ancestor::div/@class='content__left']"))
        self.assertEqual(driver.find_element_by_xpath("//a[ancestor::div/@class='organic__subtitle typo typo_type_greenurl'][1]").text, 'tensor.ru')
        #assert 'tensor.ru' == driver.find_element_by_xpath("//a[ancestor::div/@class='organic__subtitle typo typo_type_greenurl'][1]").text
        time.sleep(2)

        def tearDown(self):
            self.driver.close()


if __name__ == '__main__':
    unittest.main()
