import os
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait as wait
from features.utilities import fixture as fx
from selenium.webdriver.support.select import Select

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def wait_element_to_be_visible(context, locator_name):
    wait(context.driver, context.max_wait).until(
        ec.visibility_of_element_located(context.locator[locator_name]),
        f'{locator_name} element is still not visible after waiting.')


def wait_all_elements_to_be_present(context, locator_name):
    wait(context.driver, context.max_wait).until(
        ec.presence_of_all_elements_located(context.locator[locator_name]),
        f'{locator_name} element is still not visible after waiting.')


def wait_element_to_be_clickable(context, locator_name):
    wait(context.driver, context.max_wait).until(
        ec.element_to_be_clickable(context.locator[locator_name]),
        f'{locator_name} element is still not clickable after waiting.')


def wait_element_to_be_present(context, locator_name):
    wait(context.driver, context.max_wait).until(
        ec.presence_of_element_located(context.locator[locator_name]),
        f'{locator_name} element is still not present after waiting.')


def wait_any_element_to_be_visible(context, locator_name):
    wait(context.driver, context.max_wait).until(
        ec.visibility_of_any_elements_located(context.locator[locator_name]),
        f'Any of the {locator_name} elements are still not visible after waiting.')


def wait_element_to_be_invisible(context, locator_name):
    wait(context.driver, context.max_wait).until(
        ec.invisibility_of_element_located(context.locator[locator_name]),
        f'{locator_name} element is still visible after waiting.')


def wait_for_number_of_windows_to_be(context, window_handles):
    wait(context.driver, context.max_wait).until(
        ec.number_of_windows_to_be(len(window_handles) + 1), 'Number of window tab has not increased after waiting.')


def wait_element_not_to_be_stale(context, locator_name):
    wait(context.driver, context.max_wait).until_not(ec.staleness_of(find_element(context, locator_name)),
                                                     f'{locator_name} element is still stale after waiting.')


def wait_page_navigation(context, page_name):
    page_url = context.directory.get('url', fx.to_snake_case(page_name))
    wait(context.driver, context.max_wait).until(ec.url_to_be(page_url),
                                                 f'{page_name} is still unnavigable after waiting.')


def wait_element_to_be_invisible(context, locator_name):
    wait(context.driver, context.max_wait).until(
        ec.invisibility_of_element_located(find_element(context, locator_name)),
        f'{locator_name} element is still visible after waiting.')


def wait_all_elements_to_be_visible(context, locator_name):
    wait(context.driver, context.max_wait).until(
        ec.visibility_of_all_elements_located(context.locators[locator_name]),
        f'All {locator_name} elements are still not visible after waiting.')


def wait_in_seconds(number):
    time.sleep(number)


def get_current_url(context):
    return context.driver.current_url


def get_all_window_handles(context):
    return context.driver.window_handles


def get_text(context, locator_name):
    wait_element_to_be_visible(context, locator_name)
    return find_element(context, locator_name).text


def get_attribute_value_from_field(context, locator_name, attribute_name):
    wait_element_to_be_present(context, locator_name)
    return find_element(context, locator_name).get_attribute(attribute_name)


def find_element(context, locator_name):
    element = context.driver.find_element(*context.locator[locator_name])
    return element


def find_elements_by_id(context, locator_name):
    elements = context.driver.find_elements(*context.locators[locator_name])
    return elements


def find_elements(context, locator_name):
    element = context.driver.find_elements(*context.locator[locator_name])
    return element


def move_to_location_of_element(context, locator_name):
    wait_element_to_be_present(context, locator_name)
    element = find_element(context, locator_name)
    context.driver.execute_script("return arguments[0].scrollIntoView();", element)
    wait_element_to_be_visible(context, locator_name)
    time.sleep(0.5)


def update_param_with_feature_data(context, data_param):
    data_value = data_param
    data_variable = fx.search_and_get_multiple_value_from_content('<(.+?)>', data_value)

    if data_variable is not None:
        for dv in data_variable:
            feature_data_key = dv['inner_value'].lower()
            data_value = data_value.replace(dv['full_value'], context.feature_data[feature_data_key])

    return data_value


def is_element_displayed(context, locator_name):
    try:
        is_displayed = find_element(context, locator_name).is_displayed()
    except (NoSuchElementException, StaleElementReferenceException):
        print('Error: Element not found.')
        is_displayed = False

    return is_displayed


def click_element(context, locator_name):
    wait_element_to_be_visible(context, locator_name)
    wait_element_to_be_clickable(context, locator_name)
    find_element(context, locator_name).click()


def click_from_the_active_selection(context, locator_name, value):
    wait_any_element_to_be_visible(context, locator_name)
    options = find_elements(context, locator_name)
    for option in options:
        if option.is_displayed() and option.text == value:
            option.click()
            break


def move_to_element_then_click(context, locator_name):
    move_to_location_of_element(context, locator_name)
    find_element(context, locator_name).click()


def enter_value(context, locator_name, value):
    wait_element_to_be_visible(context, locator_name)
    wait_element_not_to_be_stale(context, locator_name)
    element = find_element(context, locator_name)
    element.clear()
    element.send_keys(value)


def select_from_checkboxes(context, label_locator_name, checkbox_locator_name):
    labels = find_elements(context, label_locator_name)
    checkboxes = find_elements(context, checkbox_locator_name)
    selected_options = []
    for row in context.table:
        selected_options.append(update_param_with_feature_data(context, row[0]))
    for index, label in enumerate(labels):
        if label.text in selected_options:
            checkboxes[index].click()


def click_and_enter_value(context, locator_name, value):
    wait_element_to_be_visible(context, locator_name)
    find_element(context, locator_name).click()
    ActionChains(context.driver).send_keys(value).perform()


def upload_file(context, locator_name, file_name):
    find_element(context, locator_name).send_keys(f'{ROOT_DIR}/uploader_files/{file_name}')


def clear_form(context, locator_name):
    locators = context.locators[locator_name]
    form_fields = None

    if type(locators) is tuple:
        wait_all_elements_to_be_visible(context, locator_name)
        form_fields = find_elements_by_id(context, locator_name)
    elif type(locators) is list:
        form_fields = []
        for locator in locators:
            form_fields.append(context.driver.find_elements_by_id(*locator))

    for form_field in form_fields:
        while form_field.get_attribute('value') != '':
            form_field.send_keys(Keys.BACKSPACE)


def clear_field(context, locator_name):
    field = find_element(context, locator_name)
    while field.get_attribute('value') != '':
        field.send_keys(Keys.BACKSPACE)
