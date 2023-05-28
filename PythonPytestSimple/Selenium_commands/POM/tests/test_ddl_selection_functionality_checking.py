import pytest

from PythonPytestSimple.Selenium_commands.POM.tests import base_test

@pytest.mark.smoke
@pytest.mark.parametrize("text", ["Green", "Yellow", "Black"])
def test_select_item_from_select_menu_and_assert_value(text):
    base_test.navigate_to_demo_qa_page()
    base_test.navigate_to_widget_part_and_select_item(text)
