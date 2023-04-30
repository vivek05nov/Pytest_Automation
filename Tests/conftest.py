from Config.config import TestData
import pytest
from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(params=["chrome"], scope="class")
def init_driver(request):
    global web_driver
    if request.param == 'chrome':
        web_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    web_driver.get(TestData.URL)
    request.cls.driver = web_driver
    yield
    web_driver.close()
