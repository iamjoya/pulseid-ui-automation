from configparser import ConfigParser, ExtendedInterpolation
from selenium import webdriver
from features.utilities import fixture as fx
from features.utilities import elements as pulse_id


def get_locators(context, key):
    locators_registry = {
        'login': pulse_id.login,
        'create_offer': pulse_id.create_offer
    }

    specific_locators = locators_registry.get(key, None)
    if specific_locators is None:
        raise LookupError('Unknown keyword: %s' % key)

    return specific_locators


def before_all(context):
    context.directory = ConfigParser(interpolation=ExtendedInterpolation())
    context.directory.read('features/utilities/page_directory.ini')
    context.max_wait = 20
    context.driver = webdriver.Chrome('drivers/chromedriver')
    context.driver.maximize_window()


def before_scenario(context, scenario):
    context.scenario_data = {}
    locators_key = fx.to_snake_case(scenario.tags[0])
    context.locator = get_locators(context, locators_key)


def after_step(context, step):
    if step.status == 'failed':
        feature_name = context.feature.name
        scenario_name = context.scenario.name
        fx.get_element_key(feature_name, scenario_name)


def after_feature(context, feature):
    context.driver.quit()
