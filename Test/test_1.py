"""
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# Chrome
driver = webdriver.Chrome('/Users/jh/Desktop/Python/selenium/Chrome_Driver/chromedriver')
# Firefox
# driver = webdriver.Firefox()
# Intenet explorer
# driver = webdriver.Ie()
driver.set_page_load_timeout(5)
driver.get("http://google.com")
driver.find_element_by_name('q').send_keys('selenium')
time.sleep(0.5)
driver.find_element_by_name('btnK').send_keys(Keys.ENTER)
time.sleep(4)

# driver.quit()
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

driver = webdriver.Chrome('/Users/jh/Desktop/Python/selenium/Chrome_Driver/chromedriver')
# driver = webdriver.Chrome('/Users/jh/Desktop/Python/selenium/Chrome_Driver/chromedriver')
wait = WebDriverWait(driver, timeout=1)
driver.get("https://google.com/")
mid_result = wait.until(presence_of_element_located((By.CLASS_NAME, "gNO89b")))
driver.find_element_by_name("q").send_keys("selenium" + Keys.RETURN)

first_result = wait.until(presence_of_element_located((By.CLASS_NAME, "rc")))

print(first_result.get_attribute("textContent"))
"""
HowToMakeWebCrawler-With-Selenium저장된 페이지2017. 2. 26. - Selenium은 주로 웹앱을 
테스트하는데 이용하는 프레임워크다. webdriver 라는 API를 통해 운영체제에 설치된 Chrome등의 브라우저를 
제어하게 ...selenium 설치selenium javaselenium 버튼 클릭크롬 드라이버 64비트selenium xpath 
사용법selenium headless함께 검색한 항목
"""
# 검색 완료 후 크롬 창 최대화
driver.maximize_window()
# 새로고침
driver.refresh()

# 3초 후 드라이버 종료(크롬창 닫힘)
time.sleep(3)
print('Test Completed')
driver.quit()
