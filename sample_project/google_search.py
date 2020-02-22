from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import HtmlTestRunner


class GoogleSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome('/Users/jh/Desktop/Python/selenium/Chrome_Driver/chromedriver')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_search_selenium(self):
        self.driver.get('https://google.com')
        self.driver.find_element_by_name('q').send_keys('selenium' + Keys.RETURN)

    def test_search_python(self):
        self.driver.get('https://google.com')
        self.driver.find_element_by_name('q1').send_keys('python' + Keys.RETURN)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print('complete')


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/jh/Desktop/Python/selenium/report'))
