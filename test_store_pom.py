import pytest
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class POM:
    @staticmethod
    def init(driver):
        POM.driver = driver

    search_box = lambda: POM.driver.find_element(By.XPATH, "//input[@placeholder='Szukaj...']")
    search_button = lambda: POM.driver.find_element(By.XPATH, "//button[@type='submit']")
    search_results = lambda: POM.driver.find_elements(By.XPATH, "//div[@class='products']/div")

    @staticmethod
    def perform_search(query):
        POM.search_box().clear()
        POM.search_box().send_keys(query)
          
@pytest.fixture(scope='module')
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--remote-allow-origins=*")
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()

EXPECTED_RESULTS = {
    "NoteBook 4 Everyone": 2,
    "School Laptop": 1,
    "NoteBook Plus": 3,
    "Business Laptop": 5,
    "Brand New Model": 4,
    "Gaming Laptop": 6,
}

@pytest.mark.parametrize("search_query", EXPECTED_RESULTS.keys())
def test_search_results(driver, search_query):
    url = "https://kodilla.com/pl/test/store"
    driver.get(url)

    POM.init(driver)
    POM.perform_search(search_query)

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@class='products']/div"))
    )
    
    results = POM.search_results()
    actual_amount = len(results)

    assert actual_amount == EXPECTED_RESULTS[search_query], f"Expected {EXPECTED_RESULTS[search_query]} but got {actual_amount} for '{search_query}'"

@pytest.mark.parametrize("search_query", EXPECTED_RESULTS.keys())
def test_search_case_insensitivity(driver, search_query):
    url = "https://kodilla.com/pl/test/store"
    driver.get(url)

    POM.init(driver)
    POM.perform_search(search_query.lower())

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@class='products']/div"))
    )
    
    results_lower = POM.search_results()
    actual_amount_lower = len(results_lower)

    POM.perform_search(search_query.upper())

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@class='products']/div"))
    )
    
    results_upper = POM.search_results()
    actual_amount_upper = len(results_upper)

    assert actual_amount_lower == actual_amount_upper, f"Results for '{search_query.lower()}' and '{search_query.upper()}' should be equal."
    assert actual_amount_lower == EXPECTED_RESULTS[search_query], f"Expected {EXPECTED_RESULTS[search_query]} but got {actual_amount_lower} for case insensitive search of '{search_query}'."

if __name__ == '__main__':
    pytest.main()
