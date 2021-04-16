Feature: Pulse ID Login

  @login @positive_scenarios
  Scenario: Login button should be disabled
    Given I went on the "PulseID Login" page
    And waited for the "Sign in with VOL" button to display
    When I click on the "Sign in with VOL" button
    And wait for the "Dev Test" message to display
    Then the "One Login" screen should be displayed
    And the following dev test message should be displayed
     """
     Connecting to Pulse Dev Cognito Test
     """

#  @login @positive_scenarios
#  Scenario Outline: Clicking not you should navigates me to the user name input field
#    Given I am on the "One Login" screen
#    When I input "<email_address>" on the "Email Address" field
#    And I click on the "Continue" button
#    And wait for the "Password" field to display
#    And I click on the "Not You?" link
#    Then the "Email Address" field should be displayed
##    And the "Email Address" field should be empty
#
#
#    Examples:
#      | email_address  |
#      | test@gmail.com |
#
#  @login @negative_scenarios
#  Scenario Outline: Validation error should prompt when I login using invalid credentials.
#    Given I am on the "One Login" screen
#    When I input "<email_address>" on the "Email Address" field
#    And I click on the "Continue" button
#    And wait for the "Password" field to display
#    And I input "<password>" on the "Password" field
#    And I click on the "Continue" button
#    And wait for the "Notification Alert" message to display
#    Then the following "Notification Alert" message should be displayed
#    """
#    Invalid username or password
#    """
#    And the following validation header message should be displayed
#     """
#     Access Denied
#     """
#    And the following validation message should be displayed
#     """
#     Please try again or contact your administrator.
#     """
#    And clicking on "Try Again" button navigates me to the "Email Address" field
#
#
#    Examples:
#      | email_address                 | password   |
#      | non.registered.user@gmail.com | uXSlk$%^sW |


  @login @negative_scenarios
  Scenario Outline: Validation error should prompt when I login using incorrect password
    Given I am on the "One Login" screen
    When I input "<email_address>" on the "Email Address" field
    And I click on the "Continue" button
    And wait for the "Password" field to display
    And I input "<password>" on the "Password" field
    And I click on the "Continue" button
    Then the following "Notification Alert" message should be displayed
    """
    Invalid username or password
    """


    Examples:
      | email_address              | password        |
      | qa-automation2@pulseid.com | invalidPassword |


  @login @positive_scenarios
  Scenario Outline: I should be able to log in on Pulse ID using correct credentials
    Given I am on the "One Login" screen
    When I input "<password>" on the "Password" field
    And I click on the "Continue" button
    And wait for the "Visa Offers Exchange" logo to display
    Then I should be navigated to the "Manage Your Offers" page
    And the "Visa Offers Exchange" logo should be displayed
    And the "Hamburger" icon should be displayed
    And the following "Dashboard" menus should be listed
      | active_menus |
      | Reports      |
      | Merchants    |
      | Offers       |
      | Settings     |
    And the following "Login user" details should be displayed
    """
    QA Automation Two
    Test Program Provider
    """

    Examples:
      | password   |
      | uXSlk$%^sW |