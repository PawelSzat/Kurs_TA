import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


def search_on_ebay(selenium, search_term):
    """
    Wyszukaj podany termin na stronie eBay.

    Args:
      selenium: Obiekt sterownika Selenium.
      search_term: Termin do wyszukania.
    """
    search_field = WebDriverWait(selenium, 10).until(
        lambda s: s.find_element(By.NAME, "_nkw")
    )
    search_field.send_keys(search_term)
    search_field.send_keys(Keys.ENTER)
    time.sleep(3)  # Odczekaj na załadowanie wyników


def verify_category_link(selenium, category_name):
    """
    Sprawdź, czy link do kategorii jest wyświetlany.

    Args:
      selenium: Obiekt sterownika Selenium.
      category_name: Nazwa kategorii do wyszukania.
    """
    category_link = WebDriverWait(selenium, 10).until(
        lambda s: s.find_element(By.LINK_TEXT, category_name)
    )
    assert category_link.is_displayed()


def test_ebay_search(selenium):
    """
    Test wyszukiwania na stronie eBay.
    """
    selenium.get("https://www.ebay.pl/")

    search_on_ebay(selenium, "Laptop")
    verify_category_link(selenium, "Laptopy i netbooki")

    selenium.quit()
