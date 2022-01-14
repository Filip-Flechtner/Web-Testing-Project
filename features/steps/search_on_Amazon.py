from behave import *

from amazon_session import *

use_step_matcher("re")


# IMPROVE: Add more assertions


@given("I am on Amazon\.com")
def step_impl(context):
    navigate_to_homepage()


@when("I search for the cheapest (?P<product>.+)")
def step_impl(context, product):
    search_for_product(product)


@then("I should see results showing the cheapest kinds of (?P<product>.+)")
def step_impl(context, product):
    assert check_if_current_title_contains(product)


@given("I have the cheapest products in my basket")
def step_impl(context):
    context.sum_of_prices = 0
    for row in context.table:
        search_for_product(row)
        cheapest_item = get_cheapest_item()
        context.sum_of_prices += cheapest_item.get_value()
        add_product_to_basket(cheapest_item)


@when("I open my basket")
def step_impl(context):
    navigate_to_basket()


@then("The basket should show the sum of the products' prices")
def step_impl(context):
    print(f"The expected sum is: {context.sum_of_prices}")
    assert context.sum_of_prices == get_subtotal_of_basket()


@given("I am not logged in")
def step_impl(context):
    assert check_if_not_logged_in()


@step("There are products in my basket")
def step_impl(context):
    for row in context.table:
        search_for_product(row)
        add_product_to_basket(get_cheapest_item())


@when("I try to go through checkout")
def step_impl(context):
    navigate_to_checkout()


@then("I should get redirected to the registration page")
def step_impl(context):
    assert check_if_current_url_contains("/ap/signin")
