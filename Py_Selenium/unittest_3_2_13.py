from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import unittest

class TestRegistration(unittest.TestCase):

    def test_registration_positive(self):
        driver = webdriver.Chrome(service=webdriver.chrome.service.Service(
            executable_path='C:\projects\Tools\chrome-driver\chromedriver.exe'))
        driver.implicitly_wait(5)

        link = "http://suninjuly.github.io/registration1.html"
        driver.get(link)

        # fill in obligatory fields
        first_name = driver.find_element(By.CSS_SELECTOR, '.first_block div:nth-child(1) input')
        first_name.send_keys('Frank')
        last_name = driver.find_element(By.CSS_SELECTOR, '.first_block div:nth-child(2) input')
        last_name.send_keys('Martin')
        email = driver.find_element(By.CSS_SELECTOR, '.first_block div:nth-child(3) input')
        email.send_keys('frank@omg.com')

        # submit form
        submit = driver.find_element(By.CSS_SELECTOR,'.btn')
        submit.click()

        # find element with welcome text
        welcome_text_elt = driver.find_element(By.TAG_NAME, "h1")
        # get text from welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        expected_welcome_message = "Congratulations! You have successfully registered!"
        self.assertEqual(welcome_text, expected_welcome_message, "Welcome message is not equal to expected message")

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        driver.quit()

if __name__ == "__main__":
    unittest.main()

