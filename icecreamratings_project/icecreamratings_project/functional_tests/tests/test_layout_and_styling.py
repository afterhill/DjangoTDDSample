from .base import FunctionalTest


class LayoutAndStylingTest(FunctionalTest):

    def test_layout_and_styling(self):
        # Edith goes to the home page
        self.browser.get(self.server_url.replace('localhost', '127.0.0.1'))
        self.browser.set_window_size(1024, 768)

        inputbox = self.get_item_input_box()

        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            515,
            delta=3
        )
