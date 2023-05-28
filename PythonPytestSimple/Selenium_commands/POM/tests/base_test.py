from PythonPytestSimple.Selenium_commands.POM.lib import helpers
from PythonPytestSimple.Selenium_commands.POM.pages import home_page
from PythonPytestSimple.Selenium_commands.POM.pages import select_menu_page


def navigate_to_demo_qa_page():
    helpers.go_to_page()

def navigate_to_widget_part_from_home_page():
    home_page.click_on_widget_part_btn()

def select_dropdown_items_from_select_page_select_menu(text="Green"):
     select_menu_page.click_on_select_btn()
     select_menu_page.select_item_from_select_menu_and_assert_text(text)

def navigate_to_widget_part_and_select_item(text="Green"):
    navigate_to_widget_part_from_home_page()
    select_dropdown_items_from_select_page_select_menu(text)


