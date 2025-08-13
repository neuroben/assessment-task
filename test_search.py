from handle_cookies import accept_cookies
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import date

BASE_URL = "https://www.esky.hu/"
TIMEOUT = 15

SEARCH_FORM = (By.ID, "qsf_form")
ROUNDTRIP_RADIO = (By.ID, "TripTypeRoundtrip")
ONEWAYTRIP_RADIO = (By.ID, "TripTypeOneway")
DEPARTURE_INPUT = (By.ID, "departureOneway")
ARRIVAL_INPUT = (By.ID, "arrivalOneway")
DEPARTURE_DATE = (By.ID, "departureDateOneway")
SEARCH_BTN = (By.CSS_SELECTOR, "button.qsf-search")
CALENDAR_TODAY = (By.XPATH, "//div[@id='ui-datepicker-div']//td[contains(@class,'ui-datepicker-today')]//a")

CITY_LIST_PARTIAL = ["Buda", "Kath"]
AIRPORT_IATA = ["BUD", "KTM"]

def test_simple_search(driver):
    driver.get(BASE_URL)

    driver.delete_all_cookies()
    accept_cookies(driver)

    WebDriverWait(driver, TIMEOUT).until(
        EC.visibility_of_element_located(SEARCH_FORM),
        message="Quick search form is not displayed"
    )

    roundtrip_radio = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located(ROUNDTRIP_RADIO),
        message="Roundtrip radio is not present"
    )

    onewaytrip_radio = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located(ONEWAYTRIP_RADIO),
        message="Onewaytrip radio is not present"
    )

    ### Oneway ticket
    if not onewaytrip_radio.is_selected():
        onewaytrip_radio.click()
        assert onewaytrip_radio.is_selected()
        assert not roundtrip_radio.is_selected()

    pick_airport(driver, DEPARTURE_INPUT, CITY_LIST_PARTIAL[0], AIRPORT_IATA[0])    

    pick_airport(driver, ARRIVAL_INPUT, CITY_LIST_PARTIAL[1], AIRPORT_IATA[1])

    departure_date = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located(DEPARTURE_DATE),
        message="Calendar is not present"
    )
    departure_date.click()

    day = WebDriverWait(driver, TIMEOUT).until(
        EC.element_to_be_clickable(CALENDAR_TODAY),
        message="Today is not clickable"
    )
    day.click()

    search_btn = WebDriverWait(driver, TIMEOUT).until(
        EC.element_to_be_clickable(SEARCH_BTN),
        message="Search button is not clickable"
    )
    search_btn.click()

    driver.implicitly_wait(5)

    page_loaded = WebDriverWait(driver, TIMEOUT).until(
        lambda d: f"/ap/{AIRPORT_IATA[0]}/ap/{AIRPORT_IATA[1]}?departureDate={date.today().isoformat()}" in d.current_url,
        message="Search results not opened"
    )

    assert page_loaded


def pick_airport(driver, input_locator, text_partial, iata):
        input = WebDriverWait(driver, TIMEOUT).until(
            EC.presence_of_element_located(input_locator),
            message="Departure input is not present"
        )

        input.click()
        for char in str(text_partial):
            input.send_keys(char)
            driver.implicitly_wait(0.05)

        target = WebDriverWait(driver, TIMEOUT).until(
            lambda d: next((e for e in d.find_elements(By.CSS_SELECTOR, f"a[data-city-code='{iata}']") if e.is_displayed()), None),
            message=f"IATA {iata} not visible"
        )

        target.click()




    

