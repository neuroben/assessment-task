from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

HOST = (By.CSS_SELECTOR, "#usercentrics-root")
DIALOG = (By.CSS_SELECTOR, "div[data-testid='uc-container']")
ACCEPT_BTN = (By.CSS_SELECTOR, "button[data-testid='uc-accept-all-button']")

def accept_cookies(driver, timeout=15):
    host = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located(HOST),
        "Usercentrics host not present"
    )
    shadow = host.shadow_root

    WebDriverWait(driver, timeout).until(
        lambda d: (el := shadow.find_element(*DIALOG)) and el.is_displayed(),
        "Cookie dialog not visible"
    )

    btn = WebDriverWait(driver, timeout).until(
        lambda d: (el := shadow.find_element(*ACCEPT_BTN)) and el.is_displayed() and el.is_enabled() and el,
        "Accept button not clickable"
    )
    btn.click()