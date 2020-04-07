# Created by Radu at 27.02.2020
Feature: User can see suggestion on main page

  Scenario Outline: Verify that Auto-suggestion works
    Given Open https://www.bestbuy.com/ page
    When Insert <search_words> in search field
    And Wait a couple of seconds
    Then See and count <expected_value> suggestions
    Examples:
      |search_words |expected_value|
      |Photo printer|12            |
      |Music player |11            |
      |TV           |12            |
      |Wifi router  |12            |