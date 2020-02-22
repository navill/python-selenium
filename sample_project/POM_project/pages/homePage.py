from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class HomePage():
    def __init__(self, driver):
        self.driver = driver
        self.welcome_link_id = 'welcome'
        self.logout_link_linktext = 'Logout'
        self.wait = WebDriverWait(self.driver, 10)

    def click_welcom(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, "welcome")))
        self.driver.find_element_by_id(self.welcome_link_id).click()

    def click_logout(self):
        self.driver.find_element_by_link_text(self.logout_link_linktext).click()
