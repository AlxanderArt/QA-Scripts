Feature: Login security
  Scenario: Locked user cannot access dashboard
    Given a locked user account
    When the user submits valid credentials
    Then the user remains on the login page
    And an account locked message is displayed
