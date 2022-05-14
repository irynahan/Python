from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    driver = webdriver.Chrome()
    driver.get(link)
    driver.find_element(By.NAME, "firstname").send_keys('Slavikus')
    driver.find_element(By.NAME, "lastname").send_keys('Leo')
    driver.find_element(By.NAME, "email").send_keys('sl@gmail.com')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    driver.find_element(By.ID,"file").send_keys(file_path)
    driver.find_element(By.XPATH,"//button[@type='submit']").click()

finally:
    time.sleep(10);
    driver.quit()