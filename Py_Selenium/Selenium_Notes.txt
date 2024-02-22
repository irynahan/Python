
# Waits Documentation

https://selenium-python.readthedocs.io/waits.html

# Expected conditions Support 7.34

https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.expected_conditions

# document.readyState  - capability pageLoadStrategy

DesiredCapabilities capabilities = new DesiredCapabilities();
capabilities.setCapability(CapabilityType.PAGE_LOAD_STRATEGY, "eager");
WebDriver driver = new FirefoxDriver(capabilities);
https://barancev.github.io/slow-loading-pages/


# Customization the Wait Class

The Wait class can be instantiated with various parameters that will change how the conditions are evaluated.

This can include:

Changing how often the code is evaluated (polling interval)
Specifying which exceptions should be handled automatically
Changing the total timeout length
Customizing the timeout message

https://www.selenium.dev/documentation/webdriver/waits/

# Packages version save to file

pip freeze > requirements.txt
pip install -r requirements.txt to install all packages in a new enwironment

# Run tests mit PyTest

pip install pytest

pytest scripts/selenium_scripts   - run all test in directory scripts/selenium_scripts

pytest test_user_interface.py	  - find and run all tests in the file test_user_interface.py

pytest scripts/drafts.py::test_register_new_user_parametrized   - find and run test with name test_register_new_user_parametrized

# Markers registration in root directory of project create file  pytest.ini
[pytest]
markers =
    smoke: marker for smoke tests
    regression: marker for regression test
after : is only description

# Run marked tests

run all tests except  pytest -s -v -m "not smoke" file.py   (-s )
run tests with one of 2 marks pytest -s -v -m "smoke or regression" file.py 
run tests wich match at the same time 2 marks pytest -s -v -m "smoke and win10" file.py 

https://docs.pytest.org/en/latest/how-to/skipping.html
https://docs.pytest.org/en/latest/reference/reference.html#pytest.mark.xfail
@pytest.mark.skip / skipif - skip a test
@pytest.mark.xfail (reason = "fix") - test fails, but we want to receive a success test execution result with a note, that this test fails; -rx to print reason in report

# Parametrisation

https://docs.pytest.org/en/latest/how-to/parametrize.html

