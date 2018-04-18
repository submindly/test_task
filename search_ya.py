import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class OrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('C:\\Python\\drivers\\chromedriver.exe')

    def test_search_in_ya(self):
        driver = self.driver
        driver.get('https://yandex.ru')
        #driver.implicitly_wait(120)
        driver.find_element_by_name('text').send_keys('Тензор')
        # suggest list
        time.sleep(1)
        self.assertTrue(driver.find_element_by_xpath("//div[ancestor::div/@class='popup__content']"))
        time.sleep(1)
        driver.find_element_by_name('text').send_keys(Keys.RETURN)
        time.sleep(1)
        self.assertIn('tensor.ru', driver.find_element_by_xpath("//a[ancestor::ul/@class='serp-list serp-list_left_yes']"))
        #driver.find_element_by_xpath("//a[ancestor::ul/@class='serp-list serp-list_left_yes']").click()
        time.sleep(2)

        def tearDown(self):
            self.driver.close()


if __name__ == '__main__':
    unittest.main()
