import time

from selenium.webdriver.common.by import By
from HRMhelper.seleniumhelper import seleniumhelper
# from selenium.webdriver.common.by import By

class Loginpage(seleniumhelper):
    company_logo= (By.XPATH, "//img[@alt='company-branding']")
    email_element = (By.XPATH, "//input[@name='username']")
    password_element = (By.XPATH, "//input[@name='password']")
    login_button = (By.XPATH, "//button[@type='submit']")
    forgot_password_link = (By.CLASS_NAME, "orangehrm-login-forgot-header")


    def __init__(self, driver): #This is the constructor of your class. It runs automatically
                                # when you create an instance of the class and expects a driver argument
                                # (usually a Selenium webdriver like webdriver.Chrome()).
        super().__init__(driver) #way to reuse the setup from the parent class.

    def login(self, username, password):
        seleniumhelper.type_text(self, self.email_element, username)
        seleniumhelper.type_text(self, self.password_element, password)
        seleniumhelper.click(self, self.login_button)
        time.sleep(10)

    def is_logo_displayed(self):
        """Verify if company logo is displayed on login page."""
        return self.is_element_visible(self.company_logo)

    def is_forgot_password_displayed(self):
        """Verify Forgot Password text is visible."""
        return self.is_element_visible(self.forgot_password_link)


