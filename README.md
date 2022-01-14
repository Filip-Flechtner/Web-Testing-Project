# Web Testing Project

## Description

This testing project uses Behave (an equivalent to Cucumber for Python) to run test cases written in the Gherkin language. The test cases are implemented using Selenium to drive Google Chrome.

## Task

> Set Up a Web Testing Project for Chrome that executes the following Test Case.
> 
> As a new Amazon user, I want to search for the cheapest Snickers and Skittles on the page.
> 
> Add the cheapest ones to your Basket and check if the basket calculates the result correctly
> 
> Check if on Checkout, without an account, the user gets redirected to the registration page.
> 
> Additional conditions:
> 
> * Document your project so a customer can use it without a personal ramp-up. (Readme.md)
> * To formulate the Test Case, please use a descriptive Language that can be exported for automated Test Reporting. (preferred: “Cucumber”)
> * Please write the Test as generic as possible to expand the Testsuite using the DRY-Principle.
> * Multiple OS Drivers should be included (Windows, Linux MacOS)

## Environment Setup

* Install Google Chrome.
* Install Python.
* Clone this repository.
* Install the project's prerequisite packages:

      pip install -r requirements.txt

## Test Execution

* Run behave from within the repository:

      behave
