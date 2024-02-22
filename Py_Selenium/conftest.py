import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    print("\nstart browser")
    driver = webdriver.Chrome(service=webdriver.chrome.service.Service(
        executable_path='C:\projects\Tools\chrome-driver\chromedriver.exe'))
    driver.implicitly_wait(5)
    yield driver
    print("\nquit browser")
    driver.quit()