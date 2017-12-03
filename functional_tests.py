from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    """docstring for NewVisitorTest."""
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith heard about the new app, she visits the site
        self.browser.get('http://localhost:8000')

        # The page title and header mentions 'to-do lists'
        self.assertIn('To-Do',self.browser.title)
        self.fail('Finish the test!')

        # She is invited to enter a to-do item straight away
        # She types "Buy peacock feathers" as an item in the to-do list

        # When she hits enter, the page updates, and now lists
        # '1: Buy peacock feathers' as first item of the to-do list

        # There is a text box to enter a second item
        # She types: "Use peacock feather to make a fly"

        # The page updates again and now shows two items

        # The site generated a unique URL, so Edith can look up her list again
        # There is also some explanatory text

        # She visits the URL and her list is there

        # Satisfied, she goes to sleep

        #browser.quit()

if __name__ == '__main__':
    unittest.main(warnings='ignore')
