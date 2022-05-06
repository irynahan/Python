from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"

    browser = webdriver.Chrome()
    browser.get(link)

    getBox = browser.find_element(By.CSS_SELECTOR, '#treasure')
    x = getBox.get_attribute('valuex')
    y = calc(x)
    get_answer_field = browser.find_element(By.CSS_SELECTOR, '#answer')
    get_answer_field.send_keys(y)
    browser.find_element(By.CSS_SELECTOR,'#robotCheckbox').click()
    browser.find_element(By.CSS_SELECTOR, '[value="robots"]').click()
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

finally:
    time.sleep(10)
    browser.quit()