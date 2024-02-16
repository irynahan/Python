import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"

# scope options “function”, “class”, “module”, “session”
@pytest.fixture(scope="function")
def driver():
    print("\nstart browser")
    driver = webdriver.Chrome(service=webdriver.chrome.service.Service(
        executable_path='C:\projects\Tools\chrome-driver\chromedriver.exe'))
    driver.implicitly_wait(5)
    yield driver
    print("\nquit browser")
    driver.quit()

# mark registration in file pytest.ini
# to run pytest -s -v -m registration file.py all tests in class
@pytest.mark.registration
class TestRegistration():

    # to run pytest -s -v -m positive file.py
    @pytest.mark.positive
    def test_registration1_positive(self, driver):

        driver.get(link1)

        # fill in obligatory fields
        first_name = driver.find_element(By.CSS_SELECTOR, '.first_block .first_class input')
        first_name.send_keys('Frank')
        last_name = driver.find_element(By.CSS_SELECTOR, '.first_block .second_class input')
        last_name.send_keys('Martin')
        email = driver.find_element(By.CSS_SELECTOR, '.first_block .third_class input')
        email.send_keys('frank@omg.com')

        # submit form
        submit = driver.find_element(By.CSS_SELECTOR,'.btn')
        submit.click()

        # find element with welcome text
        welcome_text_elt = driver.find_element(By.TAG_NAME, "h1")
        # get text from welcome_text_elt
        welcome_text = welcome_text_elt.text

        # check if registration was successful
        expected_welcome_message = "Congratulations! You have successfully registered!"
        assert welcome_text == expected_welcome_message, "Welcome message is not equal to expected message"

        # pause to check result
        time.sleep(5)

    @pytest.mark.negative
    def test_registration2_negative(self, driver):

        driver.get(link2)

        # fill in obligatory fields - no suchElementEx last_name
        first_name = driver.find_element(By.CSS_SELECTOR, '.first_block .first_class input')
        first_name.send_keys('Frank')
        last_name = driver.find_element(By.CSS_SELECTOR, '.first_block .second_class input')
        last_name.send_keys('Martin')
        email = driver.find_element(By.CSS_SELECTOR, '.first_block .third_class input')
        email.send_keys('frank@omg.com')

        # submit form
        submit = driver.find_element(By.CSS_SELECTOR, '.btn')
        submit.click()

        # find element with welcome text and get text
        welcome_text = driver.find_element(By.TAG_NAME, "h1").text

        # check if registration was successful
        expected_welcome_message = "Congratulations! You have successfully registered!"
        assert welcome_text == expected_welcome_message, "Welcome message is not equal to expected message"
