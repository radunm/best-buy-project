# Created by Radu at 4.03.2020
Feature: User is able to add multiple items to the Shopping Cart

  Scenario: User is able to add multiple items to the Shopping Cart
    Given Open https://www.bestbuy.com/ page
    When Insert smart watch into search field
    Then On search results page choose 3 element and click it
    When Add product to shopping cart
    Then Return to product search page
    Then On search results page choose 6 element and click it
    When Add product to shopping cart
    Then Expected products would be in cart
    And Close all pop-ups