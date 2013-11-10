from .base import FunctionalTest

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(FunctionalTest):

    def test_can_start_a_list_and_retrieve_it_later(self):
        url = self.server_url
        url = url.replace('localhost', '127.0.0.1')
        self.browser.get(url)

        self.assertIn('To-Do lists', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        inputbox = self.get_item_input_box()

        self.assertRegexpMatches(inputbox.get_attribute('placeholder'),
                                 'Enter a to-do item')

        inputbox.send_keys('Buy peacock features')
        inputbox.send_keys(Keys.ENTER)

        self.check_for_row_in_list_table('1: Buy peacock features')

        inputbox = self.get_item_input_box()

        inputbox.send_keys('Use peacock features to make a fly')
        inputbox.send_keys(Keys.ENTER)

        self.check_for_row_in_list_table(
            '2: Use peacock features to make a fly')

        edith_list_url = self.browser.current_url
        self.assertRegexpMatches(edith_list_url, '/lists/.+')

        self.browser.quit()
        self.browser = webdriver.Chrome()
        self.browser.get(self.server_url.replace('localhost', '127.0.0.1'))

        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock features', page_text)
        self.assertNotIn('make a fly', page_text)

        inputbox = self.get_item_input_box()
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)

        francis_list_url = self.browser.current_url
        self.assertRegexpMatches(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock features', page_text)
        self.assertIn('Buy milk', page_text)
