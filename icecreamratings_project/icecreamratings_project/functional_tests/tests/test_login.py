from .base import FunctionalTest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


TEST_EMAIL = 'studreamer@163.com'
TEST_PASSWORD = 'studreamer'


class LoginTest(FunctionalTest):

    def wait_for_element_with_id(self, element_id):
        WebDriverWait(self.browser, timeout=20).until(
            lambda b: b.find_element_by_id(element_id))

    def switch_to_new_window(self, text_in_title):
        retries = 50
        while retries > 0:
            for handle in self.browser.window_handles:
                self.browser.switch_to_window(handle)

                if text_in_title in self.browser.title:
                    return

            retries -= 1
            time.sleep(0.2)

        self.fail('Could not find the specified window' + text_in_title)

    def test_login_with_persona(self):

        self.browser.get(self.server_url)
        self.browser.find_element_by_id('login').click()

        self.switch_to_new_window('Mozilla Persona')

        self.browser.find_element_by_id(
            'authentication_email').send_keys(TEST_EMAIL)
        self.browser.find_element_by_tag_name('button').click()

        self.wait_for_element_with_id('authentication_email')
        self.browser.find_element_by_id(
            'authentication_password').send_keys(TEST_PASSWORD)
        self.browser.find_element_by_id(
            'authentication_password').send_keys(Keys.ENTER)

        self.switch_to_new_window('To-Do')

        self.wait_for_element_with_id('logout')

        navbar = self.browser.find_element_by_css_selector('.navbar')

        self.assertIn(TEST_EMAIL, navbar.text)
