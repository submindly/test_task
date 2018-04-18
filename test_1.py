import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def init_driver():
    driver = webdriver.Chrome('C:\\Python\\drivers\\chromedriver.exe')
    driver.wait = WebDriverWait(driver, 5)
    return driver


def lookup(driver, query):
    driver.get("http://yandex.ru")
    try:
        box = driver.wait.until(EC.presence_of_element_located(
            (By.NAME, "text")))
        box.send_keys(query)
        assert box.find_element_by_xpath("//div[ancestor::div/@class='popup__content']")
        time.sleep(2)
        box.send_keys(Keys.RETURN)
    except TimeoutException:
        print("Box or Button not found in google.com")


if __name__ == "__main__":
    driver = init_driver()
    lookup(driver, "")
    time.sleep(2)
    driver.quit()

#/html/body/div[5]/div