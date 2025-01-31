import pytest
from selenium import webdriver


@pytest.fixture()
def setup(browser):
        global driver
        if browser == 'chrome':
            print("Launching Chrome Browser")
            driver = webdriver.Chrome()
        elif browser == 'firefox':
            print("Launching Firefox Browser")
            driver = webdriver.Firefox()
        elif browser == 'edge':
            print("Launching Edge Browser")
            driver = webdriver.Edge()
    # if browser == 'headless':
        else:
            print("Headless mode")
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument("headless")
        # driver = webdriver.Chrome(options= chrome_options)
            driver = webdriver.Chrome()
        driver.maximize_window()
        yield driver  #
        driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser",action="store",default="chrome",help="specify the browser: chrome or firefox or edge")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")
