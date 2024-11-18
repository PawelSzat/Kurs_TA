"""
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

def test_store_search(selenium):
    selenium.get("https://kodilla.com/pl/test/store")
    search = WebDriverWait(selenium, 60).until(
        lambda s: s.find_element(By.NAME, "search")
    )
    search.send_keys("School")
    time.sleep(3)
    selenium.quit()
"""
#musialem zmienic nazwe pliku ze wzgledu na problem z uprawnieniami
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

def test_ebay_search(selenium):
    
    selenium.get("https://www.ebay.pl/")

    search_field = WebDriverWait(selenium, 60).until(
        lambda s: s.find_element(By.NAME, "_nkw")
    )

    search_field.send_keys("Laptop")

    search_field.send_keys(Keys.ENTER)

    time.sleep(3)

    category_link = WebDriverWait(selenium, 10).until(
        lambda s: s.find_element(By.LINK_TEXT, "Laptopy i netbooki")
    )
    assert category_link.is_displayed()

    selenium.quit()
