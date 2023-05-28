from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from PythonPytestSimple.Selenium_commands.POM.lib import driver
from PythonPytestSimple.Selenium_commands.TestingData import test_data
from os import path


driver = driver.get_driver_by_name()
actions = ActionChains(driver)


def go_to_page(url=test_data.url, new_window=False):
    if new_window:
        driver.execute_script(f"window.open('{url}');")
    else:
        driver.get(url)
        driver.maximize_window()

def find(loc, timeout=10, get_text=False, get_attribute=False):
    elem = WebDriverWait(driver, timeout).until(ec.presence_of_element_located(loc))
    if get_text:
        return elem.text
    elif get_attribute:
        return elem.get_attribute(get_attribute)
    return elem


def find_and_click(loc, timeout=10):
    elem = find(loc, timeout)
    driver.execute_script("arguments[0].scrollIntoView();", elem)
    elem.click()


def find_and_send_keys(loc, inp_text, timeout=10):
    elem = find(loc, timeout)
    driver.execute_script("arguments[0].scrollIntoView();", elem)
    elem.send_keys(inp_text)


def switch_window(window_id=0):
    driver.switch_to.window(driver.window_handles[window_id])


def switch_to_alert():
    return driver.switch_to.alert


def refresh_page():
    driver.refresh()


def focus_on_element(element):
    actions.move_to_element(element).perform()


def scroll_to(element):
    driver.execute_script("arguments[0].scrollIntoView();", element)


def is_displayed(element):
    element.is_displayed()


def is_selected(element):
    element.is_selected()
    return True

def select_item(loc, timeout=10, index=1, text="", value=1, by_index: bool = False, by_text: bool = False,
                    by_value: bool = False):
    select = Select(find(loc, timeout))
    if by_index:
        select.select_by_index(index)
    elif by_text:
        select.select_by_visible_text(text)
    elif by_value:
        select.select_by_value(value)
    selected_option = select.first_selected_option
    return selected_option.text

def get_file_in_temp_folder(FName):
    return path.join(path.dirname(path.dirname(path.realpath(__file__))), 'testdata\\' + FName)
