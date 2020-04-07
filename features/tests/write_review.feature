# Created by Radu at 10.03.2020
Feature: User is able to write a review

  Scenario: User is able to write a review
    Given Open https://www.bestbuy.com/ page
    When Insert Wifi router into search field
    Then On search results page choose 4 element and click it
    When Click review button
    Then Expected product has Write a Review button