import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from testData.constants import Constants


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--ignore-certificate-error')
    if browser_name == "chrome":
        s = Service("F:\packages\chromedriver.exe")
        driver = webdriver.Chrome(service=s, options=chrome_options)
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="F:\packages\geckodriver.exe")
        s = Service("F:\packages\geckodriver.exe")
        driver = webdriver.Firefox(service=s)
    elif browser_name == "IE":
        print("IE driver")

    driver.get("http://flipkart.com/")
    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()

