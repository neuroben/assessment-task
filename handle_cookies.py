from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def _shadow_query(driver, host_selector, inner_selector):
    return driver.execute_script("""
const host = document.querySelector(arguments[0]);
if(!host || !host.shadowRoot) return null;
return host.shadowRoot.querySelector(arguments[1]);
""", host_selector, inner_selector)

def _wait_for_uc_dialouge(driver, host_sel, inner_sel, timeout=10):
    return WebDriverWait(driver, timeout).until(
        lambda d: (el := _shadow_query(d, host_sel, inner_sel)) and el.is_displayed() and el
    )

def _wait_for_accept_btn(driver, host_sel, inner_sel, timeout=10):
    return WebDriverWait(driver, timeout).until(
        lambda d: (el := _shadow_query(d, host_sel, inner_sel)) and el.is_displayed() and el.is_enabled() and el
    )

def accept_cookies(driver, timeout=15):
    host = "#usercentrics-root"
    dialog_selector = "div[data-testid='uc-container']"
    button_selector = "button[data-testid='uc-accept-all-button']"

    _wait_for_uc_dialouge(driver, host, dialog_selector, timeout)
    btn = _wait_for_accept_btn(driver, host, button_selector, timeout)
    btn.click()