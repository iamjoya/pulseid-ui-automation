Feature: Pulse ID - Offer Ruleset and Offer Creation flow

  @create_offer @positive_scenarios
  Scenario Outline: Navigated to Offers Create page when i select create from the navigation menu
    Given I went on the "PulseID Login" page
    And waited for the "Sign in with VOL" button to display
    When I click on the "Sign in with VOL" button
    And I input "<email_address>" on the "Email Address" field
    And I click on the "Continue" button
    And wait for the "Password" field to display
    And I input "<password>" on the "Password" field
    And I click on the "Continue" button
    And wait for the "Manage Your Offers" page navigation
    And I click on the "<menu_link>" drawer
    And wait for the active "Sub Menu" links to display
    And I select the "<submenu_link>" link from the active "Sub Menu" links
    And wait for the "Offers Create" page navigation
    Then the "Offer Dashboard" section should be displayed
    And the "Create New Offer" button should be displayed
    And the "Overview" section should be displayed
    And the following "Overview" cards should be listed
      | overview_cards |
      | Offer Rules    |
      | Pending Review |
      | Listed         |
    And the following "How to publish your offer" cards should be listed
      | publish_cards             |
      | Create offer rule         |
      | Personalize offer content |
      | Publish offer             |


    Examples:
      | email_address              | password   | menu_link | submenu_link |
      | qa-automation2@pulseid.com | uXSlk$%^sW | Offers    | Create       |


  @create_offer @positive_scenarios
  Scenario: Navigated to rule set page when i click offer rules card
    Given I am on the "Offer Dashboard" section
    When I click on the "Offer Rules" button
    And wait for the "Offer Rule Set" page navigation
    Then the "Manage Your Offer Rules" section should be displayed
    And the "Active" menu should be displayed
    And the "Inactive" menu should be displayed
    And the "Search Offer Rule" field should be displayed
    And the "Sort Offer Rules" dropdown should be displayed
    And the "View Pagination" dropdown should be displayed
    And the following rows should be present in "Offer Rule" table
      | offer_rule                                                      | last_updates            | action_button |
      | Get $2 Cashback when you spend $12 or more on your 3rd purchase | 2020-05-20 12:06 PM UTC | Create Offer  |
      | Get 20% Cashback when you spend $50 or more                     | 2020-08-17 12:17 AM UTC | Create Offer  |
      | Get $5 Cashback when you spend $25 or more on your 4th purchase | 2020-08-11 01:22 AM UTC | Create Offer  |
      | Get 55% Cashback when you spend $1 or more on your 3rd purchase | 2020-08-11 12:00 PM UTC | Create Offer  |
      | Get 5% Cashback                                                 | 2020-08-11 12:11 PM UTC | Create Offer  |

#Note: Then step will fail (Known issue as per Sonny)
  @create_offer @positive_scenarios
  Scenario Outline: No results found should display when i search Invalid offer rule
    Given I am on the "Manage Your Offer Rules" section
    When I input "<invalid_offer_rules>" on the "Search Offer Rule" field
    And wait for background processes to finish after 2.0 seconds
    Then the following rows should be present in "Offer Rule" table
      | offer_rule                                     | last_updates            | action_button |
      | Get $150 Cashback when you spend $1500 or more | 2021-04-14 03:59 PM UTC | Create Offer  |


    Examples:
      | invalid_offer_rules   |
      | Offer rules not exist |

#Note: Then step will fail (Known issue as per Sonny)
  @create_offer @negative_scenarios
  Scenario Outline: Be able to search existing Active Offer Rules
    Given I am on the "Manage Your Offer Rules" section
    When I clear out the "Search Offer Rule" field
    And I input "<offer_rules>" on the "Search Offer Rule" field
    And wait for background processes to finish after 2.0 seconds
    Then the following rows should be present in "Offer Rule" table
      | offer_rule                                     | last_updates            | action_button |
      | Get $150 Cashback when you spend $1500 or more | 2021-04-14 03:59 PM UTC | Create Offer  |


    Examples:
      | offer_rules                                    |
      | Get $150 Cashback when you spend $1500 or more |


  @create_offer @positive_scenarios
  Scenario Outline: Be able to click and select sort by options
    Given I am on the "Manage Your Offer Rules" section
    When I clear out the "Search Offer Rule" field
    And I click on the "Sort Offer Rules" dropdown
    And I select the "<sort_by_options>" link from the active "Sort Offer Rules" options
    And wait for background processes to finish after 2.0 seconds
    Then the following rows should be present in "Offer Rule" table
      | offer_rule                                                      | last_updates            | action_button |
      | Get $2 Cashback when you spend $12 or more on your 3rd purchase | 2020-05-20 12:06 PM UTC | Create Offer  |
      | Get $5 Cashback when you spend $25 or more on your 4th purchase | 2020-08-11 01:22 AM UTC | Create Offer  |
      | Get 55% Cashback when you spend $1 or more on your 3rd purchase | 2020-08-11 12:00 PM UTC | Create Offer  |
      | Get 5% Cashback                                                 | 2020-08-11 12:11 PM UTC | Create Offer  |
      | Get $12 Cashback                                                | 2020-08-13 08:31 AM UTC | Create Offer  |
    And clicking on "Back" link navigates me to the "Offer Dashboard" section

    Examples:
      | sort_by_options             |
      | Last updated (oldest first) |


  @create_offer @positive_scenarios
  Scenario: Be able to click and select sort by options
    Given I am on the "Offer Dashboard" section
    When I click on the "Create New Offer" button
    Then the "Choose an offer rule" screen should be displayed
    And the following "offer rule" description should be displayed
    """
    What rule do you want to use for your offer?
    """
    And the "Select Offer Rule" dropdown should be displayed
    And the "Offer Rule Search" field should be displayed
    And the "Create new offer rule" button should be displayed
    And the "Back" button should be displayed
    And the "Next" button should be disabled


  @create_offer @negative_scenarios
  Scenario Outline: No offer rule should be displayed when i search invalid keyword
    Given I am on the "Choose an offer rule" screen
    When I input "<invalid_offer_rules>" on the "Offer Rule Search" field
    Then the following search result message should be displayed
    """
    No offer rule
    """

    Examples:
      | invalid_offer_rules |
      | Invalid Offer Rules |


  @create_offer @positive_scenarios
  Scenario Outline: Be able to click and select sort by options
    Given I am on the "Choose an offer rule" screen
    When I clear out the "Offer Rule Search" field
    When I input "<offer_rules>" on the "Offer Rule Search" field
    And wait for the "Progress" loader to be hidden
    And I select the "<offer_rules>" link from the active "Searched Offer Rule" options
    Then the "Select Offer Rule dropdown" should be "Get 20% Cashback when you spend $50 or more"
    And the "Offer Rule Card" details should be displayed
    And clicking on "Next" button navigates me to the "Choose a merchant" section
    And the following "merchant offer" description should be displayed
    """
    Which merchant is this offer for?
    """
    And the "Next" button should be disabled

    Examples:
      | offer_rules                                 |
      | Get 20% Cashback when you spend $50 or more |


  @create_offer @negative_scenarios
  Scenario Outline: No merchants found should be displayed when i search invalid keyword
    Given I am on the "Choose a merchant" section
    When I input "<merchant>" on the "Search Merchant" combo box
    Then the following search result message should be displayed
    """
    No merchants found
    """

    Examples:
      | merchant            |
      | Invalid Offer Rules |


  @create_offer @positive_scenarios
  Scenario Outline: Be able to search and select merchants
    Given I am on the "Choose a merchant" section
    When I clear out the "Search Merchant" combo box
    And I input "<merchant>" on the "Search Merchant" combo box
    And wait for the "Progress" loader to display
    And wait for the "Progress" loader to be hidden
    And I select the "<merchant>" link from the active "Searched Merchant" option
    Then the "Select Merchant dropdown" should be "<merchant>"
    And the "Which industry merchant is dropdown" should be "Cafe"
    And the "Merchant" logo should be displayed

    Examples:
      | merchant    |
      | Swarovskiii |


  @create_offer @negative_scenarios
  Scenario: Validation toast message should prompt when i upload invalid file
    Given I am on the "Choose a merchant" section
    When I upload the file "invalid_photo.png" in the "Add Photo" uploader
    Then the following validation toast message should be displayed
    """
    Photo should be 120px width by 120px tall in JPG or PNG file types.
    """


  @create_offer @positive_scenarios
  Scenario: Be able to upload valid file and navigated to Sales Chanel
    Given I am on the "Choose a merchant" section
    And waited for the "Validation toast" message to be hidden
    When  I upload the file "merchant_photo.jpeg" in the "Add Photo" uploader
    And wait for the "Progress" loader to display
    And wait for the "Progress" loader to be hidden
    And wait for the "Successful toast" message to display
    And wait for the "Successful toast" message to be hidden
    Then clicking on "Next" button navigates me to the "Sales Chanel" section
    And the following "Do you want to target specific channel of purchase for this reward" options should be listed
      | sales_chanel_options                                                       |
      | No, I want to target both e-commerce and in-store sales channelRECOMMENDED |
      | Yes, I want to target specific sales channel                               |


  @create_offer @positive_scenarios
  Scenario: Clicking the Yes, I want to target specific sales channel should prompt the select chanel cards
    Given I am on the "Sales Chanel" section
    When I select the following radio button in "Do you want to target specific channel of purchase for this reward?" options
      | sales_chanel_options                         |
      | Yes, I want to target specific sales channel |
    Then the following "Offer Sales Chanel" card should be listed
      | sales_chanel_options |
      | E-COMMERCE           |
      | IN-STORE             |


  @create_offer @positive_scenarios
  Scenario: Clicking E-commerce should show tips
    Given I am on the "Sales Chanel" section
    When I select the "E-COMMERCE" card from the active "Offer Sales Chanel" card
    Then the following sticky tips should be displayed
    """
    Selecting E-Commerce can help you tailor your offers and attract your customers exclusively to the online sales channels like e-commerce sites.
    """


  @create_offer @positive_scenarios
  Scenario: Clicking In-store should show tips
    Given I am on the "Sales Chanel" section
    When I select the "IN-STORE" card from the active "Offer Sales Chanel" card
    Then the following sticky tips should be displayed
    """
    Selecting In-Store can help you tailor your offers and attract your customers exclusively to the offline sales channels like your stores or malls.
    """


  @create_offer @positive_scenarios
  Scenario: Be able to complete Sales Chanel step and navigated to Your offer's content
    Given I am on the "Sales Chanel" section
    When I select the following radio button in "Do you want to target specific channel of purchase for this reward?" options
      | sales_chanel_options                                                       |
      | No, I want to target both e-commerce and in-store sales channelRECOMMENDED |
    Then clicking on "Next" button navigates me to the "Your offer's content" section
    And the value of "Create an offer title" field should be "Get 20% Cashback when you spend $50..."
    And the following "Describe what you'll offer" text should be displayed
    """
    Put yourself in a customers's shoes. Some information may seem obvious, but be detailed so customers can know more about the what you offer for them.
    """
    And the "Preview" card should be displayed
    And the "Next" button should be disabled


  @create_offer @positive_scenarios
  Scenario Outline: Be able to see the description from the preview card
    Given I am on the "Your offer's content" section
    When I click on the "Describe what you'll offer" field
    And I input to send "<description>" on the "Describe what you'll offer" field
    And wait for background processes to finish after 0.9 seconds
    Then the following preview Describe what you'll offer text should be displayed
    """
    <description>
    """
    And the following preview offer title should be displayed
    """
    Get 20% Cashback when you spend $50...
    """
    And clicking on "Next" button navigates me to the "Terms & Conditions" section


    Examples:
      | description                                              |
      | This is an automated test for Describe what you'll offer |


  @create_offer @positive_scenarios
  Scenario Outline: Be able to see the Terms and Conditions from the preview card
    Given I am on the "Terms & Conditions" section
    When I click on the "Terms & Conditions" field
    And I input to send "<terms_and_conditions>" on the "Terms & Conditions" field
    And wait for background processes to finish after 0.9 seconds
    Then the following preview terms & conditions should be displayed
    """
    <terms_and_conditions>
    """
    And clicking on "Next" button navigates me to the "Promotion Period" section


    Examples:
      | terms_and_conditions                               |
      | This is an automated test for Terms and Conditions |


  @create_offer @positive_scenarios
  Scenario: Be able to see the Promotion Period from the preview card
    Given I am on the "Promotion Period" section
    Then the following "Promotion Period" option should be listed
      | promotion_options                             |
      | No, let's keep rewarding customersRECOMMENDED |
      | Yes, let me set the promotion period          |
    And the following promotion tips message should be displayed
    """
    To get more reach and redemption, we suggest run your offer for 3 months or above
    """
    And the following sticky tips should be displayed
    """
    You don't need to set a time limit for your promotion. You can pause a live promotion at any time.
    """


  @create_offer @positive_scenarios
  Scenario Outline: Be able to select start date and view the end date
    Given I am on the "Promotion Period" section
    When I select the following radio button in "Promotion Period" option
      | promotion_options                    |
      | Yes, let me set the promotion period |
    And I clear out the "Start date" field
    And I input "<start_date>" on the "Start date" field
    Then the value of "End Date" field should be "<end_date>"
    And clicking on "Skip to preview" button navigates me to the "Summary Section" section


    Examples:
      | start_date   | end_date    |
      | Apr 26, 2021 | May 3, 2021 |


  @create_offer @positive_scenarios
  Scenario: Offer content details should be displayed
    Given I am on the "Summary Section" section
    Then the following offer content details should be displayed
    """
    Swarovskiii
    All
    Sales Channel
    Not Applicable
    Shopper Limit
    Apr 26 - May 03, 2021
    Promotion Period
    """

  @create_offer @positive_scenarios
  Scenario: Be able to click back and edit promotion period
    Given I am on the "Summary Section" section
    When I move to click on the "Back" link
    And I click on the "Back" button
    And wait for the "Redeem limit" section to display
    And I click on the "Back" button
    Then the "Promotion Period" section should be displayed


  @create_offer @positive_scenarios
  Scenario: Be able display limit field on redeem section
    Given I am on the "Promotion Period" section
    When I select the following radio button in "Promotion Period" option
      | promotion_options                             |
      | No, let's keep rewarding customersRECOMMENDED |
    And I click on the "Next" button
    And wait for the "Redeem Limit" section to display
    And I select the following radio button in "Redeem" option
      | redeem_options      |
      | Yes, choose a limit |
    Then the value of "Redeem Limit" field should be "0"
    And the following sticky tips should be displayed
    """
    To help control costs, set a limit on the number of customers who can redeem your offer. The offer will automatically terminate when this limit is reached.
    """
    And the "Next" button should be disabled
    And the "Skip to preview" button should be displayed


  @create_offer @positive_scenarios
  Scenario: Be able complete redeem step
    Given I am on the "Redeem Limit" section
    When I select the following radio button in "Redeem" option
      | redeem_options                    |
      | No, let's keep it openRECOMMENDED |
    And I click on the "Next" button
    Then the "Add photos to your offer" section should be displayed


  @create_offer @negative_scenarios
  Scenario: Validation toast message should prompt when i upload invalid image
    Given I am on the "Add photos to your offer" section
    When I upload the file "invalid_photo.png" in the "Add photo offer" uploader
    And wait for the "validation toast" message to display
    Then the following validation toast message should be displayed
    """
    Photo should be 700px width by 700px tall in JPG or PNG file types.
    """

  @create_offer @positive_scenarios
  Scenario: Be able complete redeem step and able to upload photo to offer section
    Given I am on the "Add photos to your offer" section
    And waited for the "validation toast" message to be hidden
    When I upload the file "offer_photo.jpeg" in the "Add photo offer" uploader
    And wait for the "Progress" loader to display
    And wait for the "Progress" loader to be hidden
    And wait for the "Successful toast" message to display
    And wait for the "Successful toast" message to be hidden
    Then the "Preview Photo Offer" uploaded should be displayed
    And clicking on "Next" button navigates me to the "Summary Section" section
    And the following "Offer Rule Details" summary should be displayed
    """
    This offer will give 20% cashback to Loyal customers who spend $50 or more.
    """
    And the "Offer Rule Details" card should be displayed
    And the "Offer Content" details should be displayed
    And the "Preview" Card should be displayed
    And the "Offer Tags" field should be displayed
    And the "Yes" button should be displayed
    And the "No, Save Changes" button should be displayed


  @create_offer @positive_scenarios
  Scenario Outline: Be able to add tag and navigated to set budget funding when click Yes
    Given I am on the "Summary Section" section
    When I input "<tags>" on the "Offer Tags" field
    And I select the "<tags>" link from the active "Searched tags" option
    And I click on the "Offer Content" Details
    And I click on the "Yes" button
    And wait for the "Set your budget" section to display
    Then the following sticky tips should be displayed
    """
    You don't need to set a fixed budget for your promotion. You can pause a live promotion at any time.
    """

    Examples:
      | tags    |
      | pulseid |


  @create_offer @positive_scenarios
  Scenario: Be able to set limit and navigated to offer summary
    Given I am on the "Set your budget" section
    And waited for the "Successful toast" message to display
    And waited for the "Successful toast" message to be hidden
    When I select the following radio button in "Set Budget" option
      | budget_options |
      | Yes            |
    And I input "300" on the "Set Budget" field
    And I click on the "Next" button
    And wait for the "Offer Funding" summary to display
    Then the following "Offer Funding" summary should be displayed
    """
    You will spend a total of $300.
    """


  @create_offer @positive_scenarios
  Scenario: Be able to complete offer summary when i click lets go for it
    Given I am on the "Offer Funding" summary
    When I click on the "Lets Go for it" button
    And wait for the "Progress" loader to be hidden
    And wait for the "Successful toast" message to display
    And wait for the "Successful toast" message to be hidden
    And wait for the "Manage Your Offers" section to display
    Then the "Active Pending review" button should be displayed


  @create_offer @positive_scenarios
  Scenario Outline: Be able to see the created offer rules
    Given I am on the "Manage Your Offers" section
    When I input "<merchant_name>" on the "Merchant Search" field
    And wait for background processes to finish after 2.0 seconds
    Then the following rows should be present in "Manage Offers" table
      | merchant    | category | budget  | chanel | promotion_period |
      | Swarovskiii | Cafe     | $300.00 | All    | No end date      |

    Examples:
      | merchant_name                          |
      | Get 20% Cashback when you spend $50... |