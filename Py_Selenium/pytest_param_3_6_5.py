import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

link = "https://stepik.org/lesson/236895/step/1"

def input_text():
    return math.log(int(time.time()-21.2))

def test_stepik_authoriz(driver):

        driver.get(link)
        # select enter for registered user
        enter_btn = WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.ID, "ember36")))
        enter_btn.click()
        # go to tab for registered user
        login_tab = WebDriverWait(driver,120).until(EC.element_to_be_clickable((By.XPATH, "//a[@data-tab-name = 'login']")))
        login_tab.click()
        # fill in fields and submit
        driver.find_element(By.NAME,"login").send_keys("EMAIL")
        driver.find_element(By.NAME, "password").send_keys("PASSWORD")
        driver.find_element(By.CSS_SELECTOR,"[class='sign-form__btn button_with-loader ']").click()

        if driver.find_element(By.XPATH, "//button[@class='again-btn white']").is_displayed():
                driver.find_element(By.XPATH, "//button[@class='again-btn white']").click()

        # give answer and submit
        time.sleep(15)
        answer_field = driver.find_element(By.XPATH, "//textarea[contains(@id,'ember')]")
        answer_field.clear()
        answer_field.send_keys(input_text())
        submit = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[class = 'submit-submission']")))
        submit.click()
        time.sleep(10)
        # check resul
        actual_message = WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"[class='smart-hints__hint']")))
        actual_message_text = actual_message.text
        assert actual_message_text == "Correct!", "The answer is wrong, expected message is: Correct!"
