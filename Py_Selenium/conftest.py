import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help='Choose browser: chrome or firefox')
# pytest -v --browser_name=firefox file_name.py
@pytest.fixture(scope="function")
def driver(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == 'chrome':
        print("\nstart chrome browser for test...")
        driver = webdriver.Chrome(service=webdriver.chrome.service.Service(executable_path='C:\projects\Tools\chrome-driver\chromedriver.exe'))
    elif browser_name == 'firefox':
        print("\nstart firefox browser for test...")
        driver = webdriver.Firefox(
            service=webdriver.firefox.service.Service(executable_path='C:\projects\Tools\geckodriver\geckodriver.exe'))
    else:
        raise pytest.UsageError('--browser_name should be chrome or firefox')

    driver.implicitly_wait(10)
    yield driver
    print("\nquit browser")
    driver.quit()