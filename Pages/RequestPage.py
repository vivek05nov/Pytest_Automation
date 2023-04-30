from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.basepage import Base
from calculation_module import calculation


class Request(Base):
    First_name = (By.CLASS_NAME, "first_name")
    Last_name = (By.CLASS_NAME, "last_name")
    Business_name = (By.CLASS_NAME, "business_name")
    Email = (By.CLASS_NAME, "email")
    Captcha = (By.CLASS_NAME, "mw100")
    Captcha_fill = (By.ID, "number")
    Submit = (By.ID, "demo")

    Login_link = (By.LINK_TEXT, "Login")
    Signup_link = (By.LINK_TEXT, "Signup")

    def __init__(self, driver):
        super().__init__(driver)

    def get_request_title(self, title):
        return self.do_get_title(title)

    def is_signup_visible(self):
        return self.is_visible(self.Signup_link)

    def is_login_visible(self):
        return self.is_visible(self.Login_link)

    def do_request(self, firstname, last_name, Business_name, email):
        self.do_send_keys(self.First_name, TestData.FIRST_NAME)
        self.do_send_keys(self.Last_name, TestData.LAST_NAME)
        self.do_send_keys(self.Business_name, TestData.BUSINESS_NAME)
        self.do_send_keys(self.Email, TestData.EMAIL)
        Cap = self.do_element_text(self.Captcha)
        Captcha = calculation(Cap)
        self.do_send_keys(self.Captcha_fill, Captcha)
        self.do_click(self.Submit)
