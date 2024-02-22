import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"

# mark registration in file pytest.ini
# to run pytest -s -v -m registration file.py all tests in class
@pytest.mark.registration
class TestRegistration():

    # to run pytest -s -v -m positive file.py   , "not positive", "positive and win10", "positive or negative"
    @pytest.mark.positive
    @pytest.mark.win10
    @pytest.mark.parametrize("firstName, lastName, email", [('Anni', 'Frank', '@gmail.com'), ('Tim', 'Mueller', '@gmx.de')])
    def test_registration1_positive(self, driver, firstName, lastName, email):

        driver.get(link1)

        # fill in obligatory fields
        first_name = driver.find_element(By.CSS_SELECTOR, '.first_block .first_class input')
        first_name.send_keys(firstName)
        last_name = driver.find_element(By.CSS_SELECTOR, '.first_block .second_class input')
        last_name.send_keys(lastName)
        email = driver.find_element(By.CSS_SELECTOR, '.first_block .third_class input')
        email.send_keys(f'{firstName}.{last_name}@{email}')

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


    # -rx to print reason in report
    #@pytest.mark.xfail(reason="under the fix")
    @pytest.mark.negative
    @pytest.mark.parametrize("firstName, lastName, email",
                             [('Anni', 'Frank', '@gmail.com'), ('Tim', 'Mueller', '@gmx.de')])
    def test_registration2_negative(self, driver, firstName, lastName, email):

        driver.get(link2)

        # fill in obligatory fields
        first_name = driver.find_element(By.CSS_SELECTOR, '.first_block .first_class input')
        first_name.send_keys(firstName)
        last_name = driver.find_element(By.CSS_SELECTOR, '.first_block .second_class input')
        last_name.send_keys(lastName)
        email = driver.find_element(By.CSS_SELECTOR, '.first_block .third_class input')
        email.send_keys(f'{firstName}.{last_name}@{email}')

        # submit form
        submit = driver.find_element(By.CSS_SELECTOR, '.btn')
        submit.click()

        # find element with welcome text and get text
        welcome_text = driver.find_element(By.TAG_NAME, "h1").text

        # check if registration was successful
        expected_welcome_message = "Congratulations! You have successfully registered!"
        assert welcome_text == expected_welcome_message, "Welcome message is not equal to expected message"
