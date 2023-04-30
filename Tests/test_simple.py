
from Config.config import TestData
from Pages.RequestPage import Request
from Tests.BaseTest import BaseTest


class TestSimple(BaseTest):

    def test_is_signup_visible(self):
        request = Request(self.driver)
        flag = request.is_signup_visible()
        assert flag

    def test_is_login_visible(self):
        request = Request(self.driver)
        flag = request.is_login_visible()
        assert flag

    def test_do_request(self):
        request = Request(self.driver)
        request.do_request(TestData.FIRST_NAME, TestData.LAST_NAME,TestData.BUSINESS_NAME,TestData.EMAIL)
