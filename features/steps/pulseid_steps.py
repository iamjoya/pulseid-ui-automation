from behave import given, then, when
from features.utilities import base_page_object as key, elements
from features.utilities import fixture as fx
from assertpy import assert_that


@given(u'I went on the "{page_name}" page')
def step_impl(context, page_name):
    page_url = context.directory.get('url', fx.to_snake_case(page_name))
    context.driver.get(page_url)


@given(u'waited for the "{element_name}" {element_type} to display')
def step_impl(context, element_name, element_type):
    element_key = fx.get_element_key(element_name, element_type)
    key.wait_element_to_be_visible(context, element_key)


@given(u'I am on the "{element_name}" {element_type}')
def step_impl(context, element_name, element_type):
    element_key = fx.get_element_key(element_name, element_type)
    key.wait_element_to_be_visible(context, element_key)


@when(u'I click on the "{element_name}" {element_type}')
def step_impl(context, element_name, element_type):
    element_key = fx.get_element_key(element_name, element_type)
    key.click_element(context, element_key)


@when(u'I input "{value}" on the "{element_name}" {element_type}')
def step_impl(context, value, element_name, element_type):
    element_key = fx.get_element_key(element_name, element_type)
    key.enter_value(context, element_key, value)


@when(u'wait for the "{element_name}" {element_type} to display')
def step_impl(context, element_name, element_type):
    element_key = fx.get_element_key(element_name, element_type)
    key.wait_element_to_be_visible(context, element_key)


@given(u'waited for the "{element_name}" {element_type} to be hidden')
def step_impl(context, element_name, element_type):
    element_key = fx.get_element_key(element_name, element_type)
    key.wait_element_to_be_invisible(context, element_key)


@when(u'I select the "{value}" {value_type} from the active "{element_name}" {element_type}')
def step_impl(context, value, value_type, element_name, element_type):
    element_key = fx.get_element_key(element_name, element_type)
    key.click_from_the_active_selection(context, element_key, value)


@when(u'wait for the "{page_name}" page navigation')
def step_impl(context, page_name):
    key.wait_page_navigation(context, page_name)


@when(u'wait for the active "{element_name}" {element_type} to display')
def step_impl(context, element_name, element_type):
    element_key = fx.get_element_key(element_name, element_type)
    key.wait_any_element_to_be_visible(context, element_key)


@when(u'wait for background processes to finish after {number:f} seconds')
def step_impl(context, number):
    key.wait_in_seconds(number)


@when(u'wait for the "{element_name}" {element_type} to be hidden')
def step_impl(context, element_name, element_type):
    element_key = fx.get_element_key(element_name, element_type)
    key.wait_element_to_be_invisible(context, element_key)


@when(u'I clear out the "{element_name}" {element_type}')
def step_impl(context, element_name, element_type):
    element_key = fx.get_element_key(element_name, element_type)
    if element_type == 'form':
        key.clear_form(context, element_key)
    else:
        key.clear_field(context, element_key)


@when(u'I input to send "{value}" on the "{element_name}" {element_type}')
def step_impl(context, value, element_name, element_type):
    element_key = fx.get_element_key(element_name, element_type)
    key.click_and_enter_value(context, element_key, value)


@when(u'I select the following {value_type} in "{element_name}" {element_type}')
def step_impl(context, value_type, element_name, element_type):
    label_key = fx.get_element_key(element_name, element_type)
    option_key = fx.get_element_key(element_name, value_type)
    key.select_from_checkboxes(context, label_key, option_key)


@when(u'I upload the file "{file_name}" in the "{element_name}" {element_type}')
def step_impl(context, file_name, element_name, element_type):
    element_key = fx.get_element_key(element_name, element_type)
    key.upload_file(context, element_key, file_name)


@when(u'I move to click on the "{element_name}" {element_type}')
def step_impl(context, element_name, element_type):
    element_key = fx.get_element_key(element_name, element_type)
    key.move_to_element_then_click(context, element_key)


@then(u'the "{element_name}" {element_type} should be displayed')
def step_impl(context, element_name, element_type):
    element_key = fx.get_element_key(element_name, element_type)
    key.wait_element_to_be_visible(context, element_key)

    assert_that(key.is_element_displayed(context, element_key)).described_as(
        f'{element_name} {element_type}').is_true()


@then(u'the following {element_name} should be displayed')
def step_impl(context, element_name):
    element_key = fx.get_element_key(element_name)
    key.wait_element_to_be_visible(context, element_key)
    expected = key.update_param_with_feature_data(context, context.text)
    actual = key.get_text(context, element_key)

    assert_that(actual.strip()).described_as(element_name).is_equal_to(expected)


@then(u'clicking on "{element_name}" {element_type} navigates me to the "{next_element_name}" {next_element_type}')
def step_impl(context, element_name, element_type, next_element_name, next_element_type):
    element_key = fx.get_element_key(element_name, element_type)
    next_element_key = fx.get_element_key(next_element_name, next_element_type)
    key.click_element(context, element_key)
    key.wait_element_to_be_visible(context, next_element_key)

    assert_that(key.is_element_displayed(context, next_element_key)).described_as(
        f'{next_element_name}_{next_element_type}').is_true()


@then(u'I should be navigated to the "{page_name}" page')
def step_impl(context, page_name):
    actual_url = key.get_current_url(context)
    expected_url = context.directory.get('url', fx.to_snake_case(page_name))

    assert_that(actual_url).described_as(f'{page_name}').is_equal_to(expected_url)


@then(u'the following "{element_name}" {element_type} should be listed')
def step_impl(context, element_name, element_type):
    element_key = fx.get_element_key(element_name, element_type)
    key.wait_all_elements_to_be_present(context, element_key)
    elements = key.find_elements(context, element_key)

    expected_items = []
    actual_items = []

    for row in context.table:
        expected_items.append(key.update_param_with_feature_data(context, row[0]))

    for element in elements:
        actual_items.append(element.text.replace('\n', ' ').strip())

    assert_that(actual_items).described_as(f'{element_name} {element_type}').is_equal_to(expected_items)


@then(u'the following rows should be present in "{element_name}" {element_type}')
def step_impl(context, element_name, element_type):
    element_key = fx.get_element_key(element_name, element_type)
    key.wait_all_elements_to_be_present(context, element_key)
    elements = key.find_elements(context, element_key)

    expected_values = []
    for row in context.table:
        row_values = []
        for item in row:
            if item in ('N/A', 'NA'):
                row_values.append('')
            else:
                row_values.append(key.update_param_with_feature_data(context, item))
        expected_values.append(tuple(row_values))

    column_count = len(expected_values[0])
    actual_values = []
    row_values = []
    for index, element in enumerate(elements):
        row_values.append(element.text.replace('\n', ' '))
        if (index + 1) % column_count == 0:
            actual_values.append(tuple(row_values))
            row_values = []

    assert_that(actual_values).described_as(f'{element_name} {element_type} values').contains(*expected_values)


@then(u'the "{element_name}" {element_type} should be disabled')
def step_impl(context, element_name, element_type):
    element_key = fx.get_element_key(element_name, element_type)
    actual_elements = key.find_elements(context, element_key)

    for element in actual_elements:
        assert_that(element.is_enabled()).described_as(f'{element_name} {element_type}').is_false()


@then(u'the "{element_name}" should be "{expected_value}"')
def step_impl(context, element_name, expected_value):
    element_key = fx.get_element_key(element_name)
    actual_value = key.get_text(context, element_key)
    expected_value = key.update_param_with_feature_data(context, expected_value)

    assert_that(actual_value).described_as(element_name).is_equal_to(expected_value)


@then(u'the {attribute_value} of "{element_name}" {element_type} should be "{expected_visible_value}"')
def step_impl(context, attribute_value, element_name, element_type, expected_visible_value):
    element_key = fx.get_element_key(element_name, element_type)

    attribute = attribute_value
    transformed_value = key.update_param_with_feature_data(context, expected_visible_value)
    expected_value = transformed_value if expected_visible_value not in ('empty', 'blank') else ''

    actual_value = key.get_attribute_value_from_field(context, element_key, attribute)
    assert_that(actual_value).described_as(f'{element_name} {element_type} is {expected_visible_value}').is_equal_to(
        expected_value)
