import os.path
import time

import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from utilities.utils import Utils
from seleniumwire.undetected_chromedriver.v2 import Chrome, ChromeOptions
import undetected_chromedriver as uc
import pytest_html
import geckodriver_autoinstaller


@pytest.fixture(autouse=True)
def setup(request, browser):
    global driver
    if browser == "chrome" or browser == None:
        '''options = {}
        chrome_options = uc.ChromeOptions()
        chrome_options.add_argument('--user-data-dir=hash')
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument('--blink-settings=imagesEnabled=false')
        chrome_options.add_argument ('--no-sandbox')
        chrome_options.add_argument("--disable-setuid-sandbox")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument('--disable-application-cache')
        driver = uc.Chrome(seleniumwire_options=options, options=chrome_options)'''
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == "ff":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser == "edge":
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    else:
        print("Invalid browser option")
    # ewait = WebDriverWait(driver, 30)
    driver.maximize_window()
    driver.get("https://mail.yahoo.com/d/folders/1")
    request.cls.driver = driver
    # request.cls.ewait = ewait
    yield
    driver.close()


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(autouse=True, scope="class")
def browser(request):
    return request.config.getoption("--browser")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])
    if report.when == "call":
        # always add url to report
        extras.append(pytest_html.extras.url("https://www.yatra.com/"))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            report_dir = os.path.dirname(item.config.option.htmlpath)
            file_name = report.nodeid.replace("::", "_") + ".png"
            destinationFile = os.path.join(report_dir, file_name)
            driver.save_screenshot(destinationFile)
            extras.append(pytest_html.extras.html("<div>Additional HTML</div>"))
        report.extras = extras
