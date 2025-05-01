
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as chromeOptions
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from datetime import datetime
import os
from pytest_html import extras


Baseurl="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
username="Admin"
password="admin123"

#----------------------
#Add command-line option
def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Browser to run tests: chrome or edge"
    )

# --------------------------
# Browser Setup Fixture
# --------------------------
@pytest.fixture(scope="class", autouse=True)
def setup(request):

    browser = request.config.getoption("--browser").lower()
    if not browser:
        browser = "chrome"
    try:
        if browser == "chrome":
            options = chromeOptions()
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920,1080")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

        elif browser == "edge":
            options = EdgeOptions()
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920,1080")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)

        else:
            raise ValueError(f"Unsupported browser: {browser}")
    except Exception as e:
        print(f"❌ WebDriver setup failed: {e}")
        raise
    request.cls.driver = driver
    yield
    driver.quit()

# Custom Metadata for HTML Report
# --------------------------
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata["Project Name"] = "OrangeHRM"
    metadata["Module Name"] = "Login"
    metadata["Tester"] = "Tester1"
    metadata["Environment"] = "QA"
    metadata["Execution Time"] = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """Hook to capture screenshot on test failure and attach to HTML report."""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        # Access the driver through item.cls
        driver = getattr(item.instance, "driver", None)
        if not driver:
            return
        #if driver is not None:
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")
            # Unique screenshot file name
        screenshot_name = f"screenshots/{item.name}_{datetime.now().strftime('%d-%m-%Y_%H-%M-%S')}.png"
        driver.save_screenshot(screenshot_name)

            # Attach to report if using pytest-html
        if "pytest_html" in item.config.pluginmanager.plugins:
            extra = getattr(report, "extra", [])
            extra.append(extras.image(screenshot_name))
            report.extra = extra


