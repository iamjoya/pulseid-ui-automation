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

    'choose_an_offer_rule_screen': (By.XPATH, '//h1[.="Choose an offer rule"]'),
    'offer_rule_description': (By.XPATH, '//span[@data-aid="rules-select-page-description"]'),
    'select_offer_rule_dropdown': (By.XPATH, '//button[@data-aid="select-item-button"]/div'),
    'offer_rule_search_field': (By.XPATH, '//input[contains(@placeholder,"Search")]'),
    'create_new_offer_rule_button': (By.XPATH, '//button[@data-aid="create-offer-rule-button"]'),
    'search_result_message': (By.XPATH, '//div[@data-aid="no-result"]'),
    'searched_offer_rule_options': (By.XPATH, '//div[contains(@class,"OfferRuleSelect__menu")]/div/div'),

    'choose_a_merchant_section': (By.XPATH, '//span[.="Choose a merchant"]'),
    'merchant_offer_description': (By.XPATH, '//span[@data-aid="subheader"]'),
    'select_merchant_dropdown': (By.XPATH, '//button[@data-aid="merchant-select-button"]/div'),
    'search_merchant_combo_box': (By.XPATH, '//input[contains(@placeholder,"Search")]'),
    'searched_merchant_option': (By.XPATH, '//div[contains(@class,"MerchantAutocomplete")]/div/div'),
    'which_industry_merchant_is_dropdown': (By.XPATH, '//div[contains(@class, "list__single-value")]'),
    'merchant_logo': (By.XPATH, '//div[@data-aid="upload-profile-photo"]/div[1]//img'),

    'sales_chanel_section': (By.XPATH, '//div[@data-aid="sales-channel-option"]'),
    'do_you_want_to_target_specific_channel_of_purchase_for_this_reward_radio_button': (By.XPATH, '//div[@data-aid="radio-select"]//button'),
    'do_you_want_to_target_specific_channel_of_purchase_for_this_reward_options': (By.XPATH, '//span[@class="RadioItem__label__35-Zy"]'),
    'offer_sales_chanel_card': (By.XPATH, '//div[contains(@class, "OfferSalesChannel__cardTitle_")]'),

    'manage_your_offer_rules_section': (By.XPATH, '//div[contains(@class, "OfferRulesetManagementHeader__title")]'),
    'active_menu': (By.XPATH, '//button[contains(., "Active")]'),
    'inactive_menu': (By.XPATH, '//button[contains(., "Inactive")]'),
    'search_offer_rule_field': (By.XPATH, '//input[@placeholder="Search offer rule"]'),
    'sort_offer_rules_dropdown': (By.XPATH, '//div[contains(@class, "OfferRulesetFilters__select__eNYW3")]/div[2]'),
    'view_pagination_dropdown': (By.XPATH, '//div[@class="pagination-bottom"]//div[@data-aid="select-single"]'),
    'offer_rule_card_details': (By.XPATH, '//div[@class="SummaryCard__body__1pGBW"]'),
    'offer_rule_table': (By.XPATH, '//div[contains(@class, "Table__ct-table__3lXxU")]/div[2]/div/div/div'),
    'sort_offer_rules_options': (By.XPATH, '//div[@class="css-15k3avv list__menu"]/div/div'),

    'your_offers_content_section': (By.XPATH, '//h1[contains(@class, "OfferTitleAndDescription")]'),
    'create_an_offer_title_field': (By.XPATH, '//input[contains(@class, "OfferTitleAndDescription")]'),
    'describe_what_youll_offer_text': (By.XPATH, '//div[@data-aid="offer-description"]'),
    'describe_what_youll_offer_field': (By.XPATH, '//div[contains(@class,"raftEditor-content")]/div/div'),
    'preview_card': (By.XPATH, '//div[@data-aid="offer-preview"]'),
    'preview_describe_what_youll_offer_text': (By.XPATH, '//div[@data-aid="offer-preview-offer-desc"]'),
    'preview_offer_title': (By.XPATH, '//div[@data-aid="offer-preview-offer-title"]'),

    'terms_and_conditions_section': (By.XPATH, '//h1[.="Terms and Conditions"]'),
    'terms_and_conditions_field': (By.XPATH, '//div[contains(@class,"raftEditor-content")]/div/div'),
    'preview_terms_and_conditions': (By.XPATH, '//div[@data-aid="offer-preview-offer-terms-and-condition"]'),

    'promotion_period_section': (By.XPATH, '//div[contains(@class,"OfferPromotionPeriod__section")]'),
    'promotion_period_radio_button': (By.XPATH, '//div[@data-aid="radio-select"]//button'),
    'promotion_period_option': (By.XPATH, '//span[@class="RadioItem__label__35-Zy"]'),
    'promotion_tips_message': (By.XPATH, '//span[@data-aid="promotion-duration-select-text"]'),
    'start_date_field': (By.XPATH, '//div[@data-aid="promotion-period-date-select"]/div[1]//input'),
    'end_date_field': (By.XPATH, '//div[@data-aid="promotion-period-date-select"]/div[3]//input'),

    'redeem_limit_section': (By.XPATH, '//div[contains(@class, "OfferRedemptionLimit__section")]'),
    'redeem_radio_button': (By.XPATH, '//div[@data-aid="radio-select"]//button'),
    'redeem_option': (By.XPATH, '//span[@class="RadioItem__label__35-Zy"]'),
    'redeem_limit_field': (By.XPATH, '//input[@data-aid="shoppers-count-input"]'),

    'add_photos_to_your_offer_section': (By.XPATH, '//div[@data-aid="offer-cashback-photos"]'),
    'add_photo_offer_uploader': (By.XPATH, '//div[@data-aid="offer-photos"]//input[@type="file"]'),
    'preview_photo_offer_uploaded': (By.XPATH, '//div[@data-aid="offer-preview-offer-images"]'),

    'summary_section_section': (By.XPATH, '//div[contains(@class,"OfferSummary__sectionContent")]'),
    'offer_content_details': (By.XPATH, '//div[@data-aid="offer-content"]/div'),
    'offer_rule_details_summary': (By.XPATH, '//div[@data-aid="offer-rule-details-summary-text"]'),
    'offer_rule_details_card': (By.XPATH, '//div[@data-aid="offer-ruleset"]//div[contains(@class, "SummaryCard__body")]'),
    'offer_rule_content_details_card': (By.XPATH, '//div[@data-aid="offer-content"]//div[contains(@class, "SummaryCard__body")]'),
    'preview_card': (By.XPATH, '//div[@class="OfferPreview__container__dPE6a"]'),
    'offer_tags_field': (By.XPATH, '//div[@data-aid="select-multi-creatable"]//input'),
    'searched_tags_option': (By.XPATH, '//div[@class="css-15k3avv list__menu"]/div/div'),
    'yes_button': (By.XPATH, '//button[.="Yes"]'),
    'no_save_changes_button': (By.XPATH, '//button[.="No, Save Changes"]'),
    'offer_funding_summary': (By.XPATH, '//span[@data-aid="offer-funding-summary-description"]'),
    'lets_go_for_it_button': (By.XPATH, '//button[.= "Let\'s go for it!"]'),

    'set_your_budget_section': (By.XPATH, '//h1[@data-aid="set-budget-page-header"]'),
    'set_budget_radio_button': (By.XPATH, '//div[@data-aid="radio-select"]//button'),
    'set_budget_option': (By.XPATH, '//span[@class="RadioItem__label__35-Zy"]'),
    'set_budget_field': (By.XPATH, '//input[@data-aid="set-budget-input"]'),

    'manage_your_offers_section': (By.XPATH, '//span[.="Manage Your Offers"]'),
    'active_pending_review_button': (By.XPATH, '//button[contains(@class, "Tab__active__31fw9")]'),
    'merchant_search_field': (By.XPATH, '//input[contains(@placeholder,"Search")]'),
    'manage_offers_table': (By.XPATH, '//div[@class="rt-td Table__ct-td__tMDL6"]/div[not(@data-aid="cell-checkbox" or @data-aid="cell-actions" or @data-aid="cell-offer-name-id")]'),


    # _____ Commons _____
    'back_link': (By.XPATH, '//button[@data-aid="back-button"]'),
    'progress_loader': (By.XPATH, '//div[contains(@class,"loading__3GduU AxiosProgressIndicator")]'),
    'sticky_tips': (By.XPATH, '//div[contains(@class, "tips")]//div[@data-aid="body"]'),
    'validation_toast_message': (By.XPATH, '//div[@id="root"]/div/div[1]//span'),
    'successful_toast_message': (By.XPATH, '//div[@id="root"]/div/div[1]//span[contains(., "uccess")]'),
    'add_photo_uploader': (By.XPATH, '//div[@data-aid="upload-profile-photo"]//input[@type="file"]'),
    'back_button': (By.XPATH, '//button[contains(@class, "ButtonBackLink__link")]'),
    'next_button': (By.XPATH, '//button[contains(@class, "Button__primary__2RLMY")][.="Next"]'),
    'skip_to_preview_button': (By.XPATH, '//button[@data-aid="btn-skip"]'),
}
