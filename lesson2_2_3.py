from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = 'http://suninjuly.github.io/selects1.html'

try:
    driver = webdriver.Chrome()
    driver.get(link)
    getnum1 = driver.find_element(By.CSS_SELECTOR,'#num1').text
    getnum2 = driver.find_element(By.CSS_SELECTOR,'#num2').text
    res = str(int(getnum1) + int(getnum2))
    driver.find_element(By.ID, 'dropdown').click()
    element = driver.find_element(By.CSS_SELECTOR, f"[value = '{res}']")
    element.click()
    time.sleep(2)
    driver.find_element(By.CLASS_NAME,'btn').click()


finally:
    time.sleep(10)
    driver.quit()