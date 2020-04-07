# Created by Radu at 1.03.2020
Feature: Shopping cart - empty state

  Scenario: Shopping cart - empty state
    Given Open https://www.bestbuy.com/ page
    When Click cart button
    Then Expected cart page will have Your cart is empty in the title