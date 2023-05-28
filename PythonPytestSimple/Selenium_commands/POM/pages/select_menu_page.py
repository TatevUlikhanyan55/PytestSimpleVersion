from hamcrest import equal_to
from selenium.webdriver.common.by import By
from PythonPytestSimple.Selenium_commands.POM.lib import helpers
from PythonPytestSimple.Selenium_commands.POM.lib.assertions import assert_that

select_btn = (By.XPATH, '(//*[@id="item-8"])[2]')
select_menu = (By.ID, 'oldSelectMenu')


def click_on_select_btn():
    helpers.find_and_click(select_btn)

def select_item_from_select_menu_and_assert_text(index=4, value="3", text="Green"):
    helpers.select_item(select_menu, by_value=True, value=value)
    selected_item = helpers.select_item(select_menu, by_text=True, text=text)
    assert_that(selected_item, equal_to(text))
    helpers.select_item(select_menu, by_index=True, text=index)



