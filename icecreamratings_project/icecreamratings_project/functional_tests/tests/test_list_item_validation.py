from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):

        self.browser.get(self.server_url)

        inputbox = self.get_item_input_box()

        inputbox.send_keys('\n')

        error = self.browser.find_element_by_css_selector('.has-error')  # 1
        self.assertEqual(error.text, "You can't have an empty list item")

        inputbox = self.get_item_input_box()
        inputbox.send_keys('Buy milk\n')
        self.check_for_row_in_list_table('1: Buy milk')  # 2

        inputbox = self.get_item_input_box()
        inputbox.send_keys('\n')

        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        inputbox = self.get_item_input_box()
        inputbox.send_keys('Make tea\n')
        self.check_for_row_in_list_table('1: Buy milk')
        self.check_for_row_in_list_table('2: Make tea')
