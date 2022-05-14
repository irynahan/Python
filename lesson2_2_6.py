from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = 'http://SunInJuly.github.io/execute_script.html'

try:
    driver = webdriver.Chrome()
    driver.get(link)
    getX = driver.find_element(By.ID, 'input_value').text
    res = math.log(abs(12*math.sin(int(getX))))
    driver.execute_script("window.scrollBy(0,150);")
    driver.find_element(By.ID, 'answer').send_keys(str(res))
    driver.find_element(By.ID, 'robotCheckbox').click()
    driver.find_element(By.CSS_SELECTOR, "[value='robots']").click()
    driver.find_element(By.CSS_SELECTOR, '.btn').click()




finally:
    time.sleep(10)
    driver.quit()