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
            driver.implicitly_wait(5)
            self.assertTrue(driver.find_element_by_name('text'))
            driver.find_element_by_name('text').send_keys('Тензор')
            driver.implicitly_wait(5)
            self.assertTrue(driver.find_element_by_xpath("//div[ancestor::div/@class='popup__content']"))
            driver.implicitly_wait(5)
            driver.find_element_by_name('text').send_keys(Keys.RETURN)
            driver.implicitly_wait(5)
            self.assertTrue(driver.find_element_by_xpath("//ul[ancestor::div/@class='content__left']"))
            self.assertEqual(driver.find_element_by_xpath("//a[ancestor::div/@class='organic__subtitle typo typo_type_greenurl'][1]").text, 'tensor.ru')
            driver.implicitly_wait(5)
        except NoSuchElementException as e:
            pass  # log

    def test_image_view_in_ya(self):
        driver = self.driver
        driver.get('https://yandex.ru')
        try:
            self.assertIn('Яндекс', driver.title)
            driver.implicitly_wait(5)
            self.assertTrue(driver.find_element_by_link_text('Картинки'))
            driver.find_element_by_link_text('Картинки').click()
            self.assertEqual(driver.current_url, 'https://yandex.ru/images/')
            driver.implicitly_wait(5)

            driver.find_element_by_class_name('image__image').click()
            driver.implicitly_wait(5)
            self.image_check()
            first_img_url = driver.find_element_by_xpath("//img[@class='image__image']").get_attribute('src')
            first_img = driver.title
            driver.implicitly_wait(5)

            driver.find_element_by_class_name('layout__nav__right').click()
            self.image_check()
            second_img = driver.title
            driver.implicitly_wait(5)
            self.assertNotEqual(first_img, second_img)
            driver.implicitly_wait(5)
            driver.find_element_by_class_name('layout__nav__left').click()
            driver.implicitly_wait(5)
            self.assertEqual(first_img_url, driver.find_element_by_xpath("//img[@class='image__image']").get_attribute('src'))

        except NoSuchElementException as e:
            pass  # log

    def image_check(self):
        '''
        Проверяем, что присутствуют изображение и кнопки вперед-назад
        '''
        self.assertTrue(self.driver.find_element_by_xpath("//img[@class='image__image']"))
        self.assertTrue(self.driver.find_element_by_class_name('layout__nav__left'))
        self.assertTrue(self.driver.find_element_by_class_name('layout__nav__right'))

        def tearDown(self):
            self.driver.close()


if __name__ == '__main__':
    unittest.main()
