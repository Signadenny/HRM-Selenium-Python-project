import time
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from HRMpages.LoginPages import *
from conftest import *
from Utilities.logger import get_logger

logger = get_logger(__name__)
@pytest.mark.smoke
@pytest.mark.usefixtures("setup")
class Test_login:
    def setup_class(self):
        logger.info("OrangeHRM test started")
        self.driver.get(Baseurl)
        self.login_page = Loginpage(self.driver)

#Check title of the page
    @pytest.mark.critical
    def test_title(self):
        try:
            logger.info("Checking title of the page")
            self.actual_title = self.login_page.get_title()
            print("Title of the page is: ", self.actual_title)
            assert self.actual_title == "OrangeHRM"
            print("Title is matching")
        except:
            logger.error("Title is not matching")
            self.driver.close()
            print("Title is not matching")

#check if logo is displayed
    @pytest.mark.sanity
    def test_Logo(self):
        self.login_page = Loginpage(self.driver)
        try:

            logger.info("Checking if logo is displayed")
            assert self.login_page.is_logo_displayed()
            print("Logo is displayed")

        except:
            logger.error("Logo not displayed")
            self.driver.close()
            print("Logo not displayed")
#Check forgot password link is displayed
    @pytest.mark.regression
    def test_forgot_password(self):
        self.login_page = Loginpage(self.driver)
        logger.info("Checking if forgot password link is displayed")
        assert self.login_page.is_forgot_password_displayed(), "❌ Forgot Password text not visible on login page"

    @pytest.mark.flaky(reruns=2, reruns_delay=3)
#check title and login functionality
    @pytest.mark.regression
    def test_valid_login(self):
        logger.info("Login test started")
        self.login_page = Loginpage(self.driver)
        self.login_page.login(username, password)
        print(self.driver.title)
        try:
            logger.info("Checking if title is displayed")
            self.actual_title = self.driver.title
            self.driver.close()
            assert self.actual_title == "OrangeHRM"
            print("Login test passed")
        except:
            logger.error("Login test failed")
            self.driver.close()
            print("Login test failed")

    def teardown_class(self):
        self.driver.quit()
        print("Browser closed")