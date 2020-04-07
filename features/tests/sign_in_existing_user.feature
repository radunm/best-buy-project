# Created by Radu at 29.02.2020
Feature: Verify that Sign-In with existing account works

  Scenario: Verify that Sign-In with existing account works
    Given Open https://www.bestbuy.com/ page
    When Click account button
    And Click Sign in button
    And Fill valid data
    And Click submit button
    Then Expected login will be complete successfully