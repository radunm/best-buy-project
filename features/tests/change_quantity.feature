# Created by Radu at 6.03.2020
Feature: Shopping cart - Change quantity

  Scenario: Shopping cart - Change quantity
    Given Open https://www.bestbuy.com/  page
    When Insert smart watch into search field
    Then On search results page choose 7 element and click it
    When Add product to shopping cart
    And Click go to cart button
    And Change quantity from 1 to 2
    Then Expected items in cart will be 2