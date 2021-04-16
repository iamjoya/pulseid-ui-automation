from selenium.webdriver.common.by import By

login = {
    'sign_in_with_vol_button': (By.XPATH, '//button[.= "Sign in with VOL"]'),
    'one_login_screen': (By.XPATH, '//div[contains(@class, "withConditionalBorder")]/div'),
    'dev_test_message': (By.XPATH, '//div[contains(@class, "withConditionalBorder")]/div[2]/div/div'),
    'email_address_field': (By.ID, 'username'),
    'password_field': (By.ID, 'password'),
    'not_you_link': (By.XPATH, '//button[contains(., "Not")]'),
    'continue_button': (By.XPATH, '//button[@type="submit"]'),

    'validation_header_message': (By.XPATH, '//span[contains(., "Access")]'),
    'validation_message': (By.XPATH, '//span[contains(., "Please")]'),
    'notification_alert_message': (By.XPATH, '//div[@type="error"]'),
    'try_again_button': (By.XPATH, '//button[contains(., "Try")]'),

    'sso_login_container': (By.XPATH, '//div[.="SSO Login"]'),

    'visa_offers_exchange_logo': (By.XPATH, '//div[contains(@class, "VisaBranding")]'),
    'dashboard_menus': (By.XPATH, '//div[contains(@class,"Menu__menu")]/button'),
    'hamburger_icon': (By.XPATH, '//button[contains(@class,"button-transparent__3y6i")]'),
    'login_user_details': (By.XPATH, '//div[contains(@class,"profile-details__container__2Zi4o")]/div[3]/span'),
}

create_offer = {

    'sign_in_with_vol_button': (By.XPATH, '//button[.= "Sign in with VOL"]'),
    'one_login_screen': (By.XPATH, '//div[contains(@class, "withConditionalBorder")]/div'),
    'email_address_field': (By.ID, 'username'),
    'password_field': (By.ID, 'password'),
    'continue_button': (By.XPATH, '//button[@type="submit"]'),

    'offers_drawer': (By.XPATH, '//button[contains(@class," menuItem__active__2yGR")][.= "Offers"]'),
    'sub_menu_links': (By.XPATH, '//div[contains(@class,"drawer__root__1EJhK")]/div[1]/div[3]/button'),

    'offer_dashboard_section': (By.XPATH, '//span[contains(@class,"Text__heading1")]'),
    'create_new_offer_button': (By.XPATH, '//div[contains(@class, "Header__foreground")]//button[@data-aid="create-offer-button"]'),
    'overview_section': (By.XPATH, '//div[@data-aid="marketplace-offer-create-overview"]'),
    'offer_rules_button': (By.XPATH, '//div[contains(@class, "Overview__infoCards")]/div[1]//button'),
    'overview_cards': (By.XPATH, '//div[@class="Overview__infoCards__3ODwo"]//span'),
    'how_to_publish_your_offer_cards': (By.XPATH, '//div[@data-aid="infographics-card-title"]'),

    'manage_your_offer_rules_section': (By.XPATH, '//div[contains(@class, "OfferRulesetManagementHeader__title")]'),
    'active_menu': (By.XPATH, '//button[contains(., "Active")]'),
    'inactive_menu': (By.XPATH, '//button[contains(., "Inactive")]'),
    'search_offer_rule_field': (By.XPATH, '//input[@placeholder="Search offer rule"]'),
    'sort_offer_rule_dropdown': (By.XPATH, '//div[contains(@class, "OfferRulesetFilters__select__eNYW3")]/div[2]'),
    'view_pagination_dropdown': (By.XPATH, '//div[@class="pagination-bottom"]//div[@data-aid="select-single"]'),
    'offer_rule_table': (By.XPATH, '//div[contains(@class, "Table__ct-table__3lXxU")]/div[2]/div/div/div'),



}