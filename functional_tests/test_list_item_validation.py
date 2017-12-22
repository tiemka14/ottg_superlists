from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys
from unittest import skip


class ItemValidationTest(FunctionalTest):
    def test_cannot_add_empty_list_items(self):
        # Edith goes to the list and accidentally tries to submit an empty list item.
        # She hits enter on the input box

        # The homepage refreshes, and there is an error message
        # Saying that lists cannot be blank

        # She tries again with some text for the item, which now works

        # Perversely she now tries to submit a second empty list item

        # She receives a similar warning on the list page
        # and she can correct it by filling some text in

        self.fail('write me!')
