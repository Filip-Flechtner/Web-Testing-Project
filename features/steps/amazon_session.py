from time import sleep

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from infrastructure.browser import driver


# IMPROVE: Replace the sleep calls with Selenium-specific wait calls
# IMPROVE: Make navigation steps more generic
# IMPROVE: Handle more exceptions


def navigate_to_homepage():
    driver.get("https://www.amazon.com")


def search_for_product(product):
    search_box = driver.find_element_by_id("twotabsearchtextbox")
    search_box.clear()
    search_box.send_keys(product)
    search_box.send_keys(Keys.ENTER)


def check_if_current_title_contains(string):
    return string in driver.title


class Product:
    def __init__(self, element):
        self.element = element

    def get_price(self):
        return self.element.get_attribute("innerText")

    def get_value(self):
        return convert_price_to_value(self.get_price())


def get_cheapest_item():
    # Sort by price in ascending order and grab the first result that has a price
    sleep(1)
    driver.find_element_by_id("a-autoid-0").click()
    driver.find_element_by_id("s-result-sort-select_1").click()
    sleep(1)
    cheapest_item = Product(driver.find_element_by_class_name("a-offscreen"))
    return cheapest_item


def convert_price_to_value(string):
    # Remove currency and whitespace, then handle the decimal separator
    # IMPROVE: Handle digit grouping separators
    value = string.strip("$€").strip()
    value = ".".join((value[0:-3], value[-2:len(value)]))
    return float(value)


def add_product_to_basket(product):
    # Open the product detail page and put the product into the basket
    actions = ActionChains(driver)
    actions.move_to_element(product.element).click().perform()
    sleep(1)
    try:
        driver.find_element_by_id("add-to-cart-button").click()
    except NoSuchElementException:
        print(f"Could not locate any button for adding product to the basket. Element: {product.element}")


def navigate_to_basket():
    driver.get("https://www.amazon.com/gp/cart/view.html?ref_=nav_cart")


def get_subtotal_of_basket():
    if driver.current_url != "https://www.amazon.com/gp/cart/view.html?ref_=nav_cart":
        navigate_to_basket()
    subtotal_element = driver.find_element_by_id("sc-subtotal-amount-activecart")
    subtotal = subtotal_element.get_attribute("innerText")
    return convert_price_to_value(subtotal)


def check_if_not_logged_in():
    account_button_link = driver.find_element_by_id("nav-link-accountList").get_attribute("href")
    return "/ap/signin" in account_button_link


def navigate_to_checkout():
    navigate_to_basket()
    sleep(1)
    checkout_button = driver.find_element_by_name("proceedToRetailCheckout")
    checkout_button.click()


def check_if_current_url_contains(string):
    return string in driver.current_url
