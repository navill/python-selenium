import unittest
import time

import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from sample_project.POM_project.pages.login_page import LoginPage
from sample_project.POM_project.pages.homePage import HomePage


class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome('/Users/jh/Desktop/Python/selenium/Chrome_Driver/chromedriver')
        # cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    def test_login(self):
        wait = WebDriverWait(self.driver, 10)
        driver = self.driver
        driver.get('https://opensource-demo.orangehrmlive.com/')
        login = LoginPage(driver)
        login.enter_username('Admin')
        login.enter_password('admin123')
        login.click_login()

        hompage = HomePage(driver)
        hompage.click_welcom()
        time.sleep(2)
        hompage.click_logout()
        """
        driver.find_element_by_id('txtUsername').send_keys('Admin')
        driver.find_element_by_id('txtPassword').send_keys('admin123' + Keys.RETURN)
        try:
            # welcom list가 뜰때까지 대기
            wait.until(EC.element_to_be_clickable((By.ID, "welcome")))
            driver.find_element_by_id('welcome').click()
            # link text('Logout')이 뜰때까지 대기
            # wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Logout")))
            wait.until(EC.presence_of_element_located((By.LINK_TEXT, "登出")))
            driver.find_element_by_link_text('Logout').click()
        except Exception as e:
            print(f'raised time out exception: {e}')
        finally:
            time.sleep(2)
        """

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print('Test Completed')


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/jh/Desktop/Python/selenium/report'))
