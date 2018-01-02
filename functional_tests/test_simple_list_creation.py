from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(FunctionalTest):
    def test_can_start_a_list_for_one_user(self):
        # Edith heard about the new app, she visits the site
        self.browser.get(self.live_server_url)

        # The page title and header mentions 'to-do lists'
        self.assertIn('To-Do',self.browser.title)

        header_text = self.browser.find_element_by_tag_name("h1").text
        self.assertIn('To-Do',header_text)

        # She is invited to enter a to-do item straight away
        inputbox = self.get_item_input_box()
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        # She types "Buy peacock feathers" as an item in the to-do list
        #inputbox.send_keys('Buy peacock feathers')

        # When she hits enter, the page updates, and now lists
        # '1: Buy peacock feathers' as first item of the to-do list
        self.add_list_item('Buy peacock feathers')

        # There is a text box to enter a second item
        # She types: "Use peacock feather to make a fly"
        self.add_list_item("Use peacock feather to make a fly")

        # The page updates again and now shows two items
        #self.wait_for_row_in_list_table('1: Buy peacock feathers')
        #self.wait_for_row_in_list_table('2: Use peacock feather to make a fly')

    def test_multiple_users_can_start_lists_at_different_urls(self):
        # Edith starts a new to-do list
        self.browser.get(self.live_server_url)
        self.add_list_item('Buy peacock feathers')

        # She notices that her list has a unique URL
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url,'/lists/.+')

        # Now a new user, Francis, comes along to the site

        ## We use a new browser session to make sure that no information
        ## of Edith's is coming through from cookies etc.
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Francis visits the homepage. There is no sign of Edith's list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers',page_text)
        self.assertNotIn('make a fly',page_text)

        # Francis starts a new list by entering a new item.
        # He is less interesting than Edith
        self.add_list_item('Buy milk')

        # Francis gets his own unique URL
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url,edith_list_url)

        # Again there is no trace of Edith's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers',page_text)
        self.assertIn('Buy milk',page_text)

        # Satisfied they both go back to sleep
        #self.fail('Finish the test!')
