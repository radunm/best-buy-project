# Created by Radu at 28.02.2020
Feature: User can search for product

  Scenario: User is taken to the search results page
    Given Open https://www.bestbuy.com/ page
    When Insert dry vacuum into search field
    Then Check that title contains "dry vacuum"