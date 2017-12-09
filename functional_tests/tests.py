from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
#import unittest

class NewVisitorTest(LiveServerTestCase):
    """Tests for new visitors."""
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id("id_list_table")
        rows = table.find_elements_by_tag_name("tr")
        self.assertIn(row_text,[row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith heard about the new app, she visits the site
        self.browser.get(self.live_server_url)

        # The page title and header mentions 'to-do lists'
        self.assertIn('To-Do',self.browser.title)

        header_text = self.browser.find_element_by_tag_name("h1").text
        self.assertIn('To-Do',header_text)

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        # She types "Buy peacock feathers" as an item in the to-do list
        inputbox.send_keys('Buy peacock feathers')

        # When she hits enter, the page updates, and now lists
        # '1: Buy peacock feathers' as first item of the to-do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # There is a text box to enter a second item
        # She types: "Use peacock feather to make a fly"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys("Use peacock feather to make a fly")
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # The page updates again and now shows two items
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feather to make a fly')

        # The site generated a unique URL, so Edith can look up her list again
        # There is also some explanatory text
        self.fail('Finish the test!')

        # She visits the URL and her list is there

        # Satisfied, she goes to sleep

        #browser.quit()

#if __name__ == '__main__':
#    unittest.main(warnings='ignore')
