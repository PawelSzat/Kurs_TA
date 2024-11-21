from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def assert_amount(driver, search_query, expected_amount):
    search_box = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Szukaj...']")
    search_box.clear()
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div.products-header h3 span"))
    )

    products_count_element = driver.find_element(By.CSS_SELECTOR, "div.products-header h3 span")
    products_count_text = products_count_element.text
    actual_amount = int(products_count_text.split()[0])

    assert actual_amount == int(expected_amount), f"Expected {expected_amount} but got {actual_amount} for {search_query}"

    WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "section > article"))
    )
    
    product_cards = driver.find_elements(By.CSS_SELECTOR, "section > article")
    
    for product in product_cards:
        print(product.text)

def test_store():
    driver = webdriver.Chrome()
    driver.get("https://kodilla.com/pl/test/store")

    try:
        assert_amount(driver, "School Laptop", "2")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_store()
