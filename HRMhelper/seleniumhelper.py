from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class seleniumhelper:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    def find_element(self, locator):
        """Find a single web element."""
        try:
            return WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            print(f"Element not found: {locator}")
            return None

    def click(self, locator):
        """Click on a web element."""
        element = self.find_element(locator)
        if element:
            element.click()
        else:
            raise Exception(f"Unable to click, element not found: {locator}")

    def type_text(self, locator, text):
        """Type text into an input box."""
        element = self.find_element(locator)
        if element:
            element.clear()
            element.send_keys(text)
        else:
            raise Exception(f"Unable to type, element not found: {locator}")

    def get_text(self, locator):
        """Get text from a web element."""
        element = self.find_element(locator)
        if element:
            return element.text
        else:
            raise Exception(f"Unable to get text, element not found: {locator}")

    def is_element_visible(self, locator):
        """Check if element is visible on the page."""
        try:
            return WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            return False

    def wait_for_element_to_be_clickable(self, locator):
        """Wait until element is clickable."""
        try:
            return WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            print(f"Element not clickable: {locator}")
            return None

    def get_title(self):
        """Get the current page title."""
        return self.driver.title

    def navigate_to(self, url):
        """Navigate to a URL."""
        self.driver.get(url)

    def is_element_displayed(self, locator):
        """Check if element is displayed."""
        try:
            return WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator)).is_displayed()
        except TimeoutException:
            return False

    def switch_to_frame(self, locator):
        """Switch into iframe using locator"""
        frame_element = self.find_element(locator)
        if frame_element:
            self.driver.switch_to.frame(frame_element)
        else:
            raise Exception(f"Unable to switch, iframe not found: {locator}")

    def switch_to_default_content(self):
        """Switch back to main page from iframe"""
        self.driver.switch_to.default_content()

# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# class seleniumhelper:
#     def __init__(self, driver):
#         self.driver = driver
#
#     def webelement_enter(self, locator, text):
#         WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(text)
#
#     def webelement_click(self, locator):
#         WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).click()

