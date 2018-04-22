import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import logging


class OrgSearch(unittest.TestCase):
    """Yandex search tests"""

    def setUp(self):
        logging.basicConfig(filename="test_results.log", level=logging.INFO)
        driver_path = "./drivers/chromedriver"
        self.driver = webdriver.Chrome(driver_path)
        self.driver.maximize_window()
        print(self.shortDescription())

    def test_first_task_search_in_ya(self):
        """Тест - Поиск в Яндексе"""
        driver = self.driver
        driver.get("https://yandex.ru")
        try:
            self.assertIn("Яндекс", driver.title)
            self.wait()
            self.assertTrue(driver.find_element_by_id("text"))
            driver.find_element_by_id("text").send_keys("Тензор")
            self.wait()
            self.assertTrue(driver.find_element_by_xpath("//div[ancestor::div/@class='popup__content']"))
            self.wait()
            driver.find_element_by_id("text").send_keys(Keys.RETURN)
            self.wait()
            self.assertTrue(driver.find_element_by_xpath("//ul[ancestor::div/@class='content__left']"))
            self.assertEqual(driver.find_element_by_xpath(
                "//a[ancestor::div/@class='organic__subtitle typo typo_type_greenurl'][1]").text, 'tensor.ru')
            self.wait()
        except NoSuchElementException as e:
            logging.error(e)

    def test_second_tesk_image_view_in_ya(self):
        """Тест - Поиск картинок в Яндексе"""
        driver = self.driver
        driver.get("https://yandex.ru")
        try:
            self.assertIn("Яндекс", driver.title)
            self.wait()
            self.assertTrue(driver.find_element_by_link_text("Картинки"))
            driver.find_element_by_link_text("Картинки").click()
            self.assertEqual(driver.current_url, "https://yandex.ru/images/")
            self.wait()

            driver.find_element_by_class_name("image__image").click()
            self.wait()
            self.image_check()
            first_img_url = driver.find_element_by_xpath("//img[@class='image__image']").get_attribute("src")
            first_img = driver.title

            driver.find_element_by_class_name("layout__nav__right").click()
            self.image_check()
            second_img = driver.title
            self.wait()
            self.assertNotEqual(first_img, second_img)
            driver.find_element_by_class_name("layout__nav__left").click()
            self.wait()
            self.assertEqual(first_img_url, driver.find_element_by_xpath("//img[@class='image__image']").get_attribute("src"))

        except NoSuchElementException as e:
            logging.error(e)

    def image_check(self):
        """Проверяем, что присутствуют изображение и кнопки вперед-назад"""
        self.assertTrue(self.driver.find_element_by_xpath("//img[@class='image__image']"))
        self.assertTrue(self.driver.find_element_by_class_name("layout__nav__left"))
        self.assertTrue(self.driver.find_element_by_class_name("layout__nav__right"))
    
    def wait(self):
        sleep(1)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
