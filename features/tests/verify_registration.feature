# Created by Radu at 29.02.2020
Feature: Verify Registration process

  Scenario: Verify that Registration flow works as expected
    Given Open https://www.bestbuy.com/ page
    When Click account button
    And Best Buy: click "Create account"
    Then Fill all fields with fake data
    When Click submit
    Then Expected registration will be complete successfully