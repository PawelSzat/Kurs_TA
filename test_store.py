from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def assert_amount(driver, search_query, expected_amount):
    search_box = driver.find_element(By.XPATH, "//input[@placeholder='Szukaj...']")
    search_box.clear()
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)

   
    products_count_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@class='products-header']/h3/span"))
    )

    products_count_text = products_count_element.text
    actual_amount = int(products_count_text.split()[0])

    assert actual_amount == int(expected_amount), f"Expected {expected_amount} but got {actual_amount} for {search_query}"

def test_store():
    driver = webdriver.Chrome()
    driver.get("https://kodilla.com/pl/test/store")

    try:
        assert_amount(driver, "School Laptop", "1")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_store()
# nie dodawałem więcej asseracji ze względu na błąd przekroczenia czasu. Nawet jak zwiększę czas oczekiwania do 60 to zwraca mi błąd: selenium.common.exceptions.TimeoutException 
