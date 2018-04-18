from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome('C:\\Python\\drivers\\chromedriver.exe')
driver.get('https://yandex.ru')
driver.implicitly_wait(120)
#driver.find_element_by_xpath('//*[@id="text"]').send_keys('Тензор')
driver.find_element_by_name('text').send_keys('Тензор')
# тут проверка что список саггестов появился
driver.find_element_by_name('text').send_keys(Keys.RETURN)

# тут таблица результатов поиска !!!!!!!!!!!!!!!!!!

driver.find_element_by_xpath("//a[ancestor::ul/@class='serp-list serp-list_left_yes']").click()