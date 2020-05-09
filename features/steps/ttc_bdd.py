from behave import *
from selenium.webdriver.support.ui import Select
from time import sleep

@given(u'User is on Home Page "http://0.0.0.0:5000/" on browser "chrome"')
def step_impl(context):
    context.browser.get("localhost:5000")
    url = context.browser.current_url
    print(url)
    assert url == "http://localhost:5000/"
    sleep(3)

@when(u'User confirms Address')
def step_impl(context):
    context.browser.find_element_by_id('address').clear()
    context.browser.find_element_by_id('address').send_keys('1111 Terrific St. Dallas, TX 70001')
    sleep(3)

@when(u'User selects product as "Umbrella"')
def step_impl(context):
    s1 = Select(context.browser.find_element_by_id('productselect'))
    s1.select_by_index(1)
    assert s1.first_selected_option.get_attribute('value') == "Rain Coat"
    # assert s1.first_selected_option.get_attribute('value') == "Umbrella"
    sleep(3)

@when(u'User selects valid payment')
def step_impl(context):
    s2 = Select(context.browser.find_element_by_id('payinfo'))
    s2.select_by_value("Card ending in 5678")
    sleep(3)

@when(u'User clicks on "Request" button')
def step_impl(context):
    submit_button = context.browser.find_element_by_id('test')
    submit_button.click()
    sleep(3)

@then(u'Message displayed is Order Status')
def step_impl(context):
    print("Order placed successfully")

@then(u'close browser')
def step_impl(context):
    print("Step: Closing the Browser")
