from selenium.webdriver.common.by import By
from PythonPytestSimple.Selenium_commands.POM.lib import helpers

widget_part_btn = (By.XPATH, '(//*[@xmlns="http://www.w3.org/2000/svg"])[4]')


def click_on_widget_part_btn():
    helpers.find_and_click(widget_part_btn)
