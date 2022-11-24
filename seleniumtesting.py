from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Safari()
url = "https://soundcloud.com/discover"
driver.get(url)
time.sleep(2)
accept_cookies_button = driver.find_element(by=By.XPATH, value='//*[@id="onetrust-accept-btn-handler"]')
accept_cookies_button.click()
