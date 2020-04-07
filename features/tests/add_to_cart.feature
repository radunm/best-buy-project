# Created by Radu at 3.03.2020
Feature: User is able to add an item to the Shopping Cart

  Scenario: User is able to add an item to the Shopping Cart
    Given Open https://www.bestbuy.com/  page
    When Insert smart watch into search field
    Then On search results page choose 3 element and click it
    When Add product to shopping cart
    Then Expected product would be in cart
    Then Close all pop-ups