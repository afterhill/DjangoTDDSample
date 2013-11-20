from .base import FunctionalTest
from lists.forms import EMPTY_LIST_ERROR, DUPLICATE_ITEM_ERROR


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):

        self.browser.get(self.server_url.replace('localhost', '127.0.0.1'))

        inputbox = self.get_item_input_box()

        inputbox.send_keys('\n')

        error = self.get_error_element()
        self.assertEqual(error.text, EMPTY_LIST_ERROR)

        inputbox = self.get_item_input_box()
        inputbox.send_keys('Buy milk\n')
        self.check_for_row_in_list_table('1: Buy milk')  # 2

        inputbox = self.get_item_input_box()
        inputbox.send_keys('\n')

        error = self.get_error_element()
        self.assertEqual(error.text, EMPTY_LIST_ERROR)

        inputbox = self.get_item_input_box()
        inputbox.send_keys('Make tea\n')
        self.check_for_row_in_list_table('1: Buy milk')
        self.check_for_row_in_list_table('2: Make tea')

    def test_cannot_add_duplicate_items(self):
        self.browser.get(self.server_url.replace('localhost', '127.0.0.1'))
        self.get_item_input_box().send_keys('Buy wellies\n')
        self.check_for_row_in_list_table('1: Buy wellies')

        self.get_item_input_box().send_keys('Buy wellies\n')

        self.check_for_row_in_list_table('1: Buy wellies')

        error = self.get_error_element()
        self.assertEqual(error.text, DUPLICATE_ITEM_ERROR)

    def test_error_message_are_cleared_on_input(self):
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('\n')
        error = self.get_error_element()


        self.get_item_input_box().send_keys('a')

        error = self.get_error_element()

        self.assertFalse(error.is_displayed())

    def get_error_element(self):
        return self.browser.find_element_by_css_selector('.has-error')
