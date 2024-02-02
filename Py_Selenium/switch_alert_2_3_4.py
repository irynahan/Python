from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = 'http://suninjuly.github.io/alert_accept.html'

def calc_res(x):
    return str(math.log(abs(12 * math.sin(x))))


try:
    driver = webdriver.Chrome(service=webdriver.chrome.service.Service(executable_path='C:\projects\Tools\chrome-driver\chromedriver.exe'))
    driver.get(link)
    driver.find_element(By.XPATH, '//button').click()
    modal = driver.switch_to.alert
    modal.accept()
    x = int(driver.find_element(By.ID, 'input_value').text)
    res = calc_res(x)
    driver.find_element(By.NAME, 'text').send_keys(res)
    driver.find_element(By.CSS_SELECTOR, "[type = 'submit']").click()

finally:
    time.sleep(10)
    driver.quit()