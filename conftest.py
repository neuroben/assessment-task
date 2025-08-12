import pytest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

@pytest.fixture
def driver():
    opts = Options()
    opts.add_argument("--start-maximized")
    opts.add_argument("--disable-notifications")
    #opts.add_argument("--headless=new")
    driver = webdriver.Chrome(options=opts)
    driver.maximize_window()
    yield driver
    driver.quit()