from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

link = 'http://suninjuly.github.io/explicit_wait2.html'

def calc_res(x):
    return str(math.log(abs(12 * math.sin(x))))

try:
    driver = webdriver.Chrome(service=webdriver.chrome.service.Service(executable_path='C:\projects\Tools\chrome-driver\chromedriver.exe'))
    driver.implicitly_wait(5)
    driver.get(link)
    expected_price = WebDriverWait(driver, 12).until(EC.text_to_be_present_in_element((By.ID,'price'), '$100'))
    driver.find_element(By.ID, 'book').click()
    x = int(driver.find_element(By.ID, 'input_value').text)
    res = calc_res(x)
    driver.find_element(By.ID,'answer').send_keys(res)
    driver.find_element(By.ID, "solve").click()

finally:
    time.sleep(10)
    driver.quit()




