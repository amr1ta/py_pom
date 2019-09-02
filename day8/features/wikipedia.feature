Feature: Wikipedia landing page feature

  Scenario: Launch wikipedia application
    Given User is on wikipedia Homepage
      When User searches "Design Pattern"
      Then Title of the page should be "Design pattern"
