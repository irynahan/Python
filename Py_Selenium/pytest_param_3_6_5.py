import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

links = ['https://stepik.org/lesson/236895/step/1','https://stepik.org/lesson/236896/step/1','https://stepik.org/lesson/236897/step/1','https://stepik.org/lesson/236898/step/1','https://stepik.org/lesson/236899/step/1','https://stepik.org/lesson/236903/step/1','https://stepik.org/lesson/236904/step/1','https://stepik.org/lesson/236905/step/1']

def input_text():
    return math.log(int(time.time()-21.2))

@pytest.mark.parametrize("address_link", links)
def test_stepik_authoriz(driver, address_link):
        driver.get(address_link)
        # select enter for registered user
        enter_btn = WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.ID, "ember36")))
        enter_btn.click()
        # go to tab for registered user
        login_tab = WebDriverWait(driver,120).until(EC.element_to_be_clickable((By.XPATH, "//a[@data-tab-name = 'login']")))
        login_tab.click()
        # fill in fields and submit
        driver.find_element(By.NAME,"login").send_keys("login")
        driver.find_element(By.NAME, "password").send_keys("password")
        driver.find_element(By.CSS_SELECTOR,"[class='sign-form__btn button_with-loader ']").click()

        try:
                solve_again = driver.find_element(By.XPATH, "//button[@class='again-btn white']")
                if solve_again.is_displayed():
                        driver.find_element(By.XPATH, "//button[@class='again-btn white']").click()
        except :
                print('Element is not found')

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
