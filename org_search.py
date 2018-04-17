import unittest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys


class OrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(
                          command_executor='http://localhost:4444/wd/hub',
                          desired_capabilities=DesiredCapabilities.CHROME)

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        assert "No results found." not in driver.page_source
        elem.send_keys(Keys.RETURN)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
