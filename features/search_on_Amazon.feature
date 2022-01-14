Feature: Searching for products on Amazon

  As a new Amazon user,
  I want to search for the cheapest Snickers and Skittles on the page.

  Background:
    Given I am on Amazon.com

    Scenario Outline: The user searches for the cheapest version of a product
      When I search for the cheapest <product>
      Then I should see results showing the cheapest kinds of <product>
      Examples:
        | product  |
        | Snickers |
        | Skittles |

    Scenario: The user adds multiple products to the basket
      Given I have the cheapest products in my basket
        | product  |
        | Snickers |
        | Skittles |
      When  I open my basket
      Then  The basket should show the sum of the products' prices

    Scenario: The user tries to go through checkout without an account
      Given I am not logged in
      And   There are products in my basket
        | product  |
        | Snickers |
        | Skittles |
      When  I try to go through checkout
      Then  I should get redirected to the registration page
