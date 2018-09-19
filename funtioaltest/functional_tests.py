from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser=webdriver.Chrome();
    def tearDown(self):
        self.browser.quit();
    def test_can_start_a_list_and_retrieve_it_later(self):
         # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get('http://localhost:8000');
        #she notices the page title and the header mantion to_do lists
        self.assertIn('To_Do',self.browser.title);
        self.fail('finished the test!');
if __name__=="__main__":
    unittest.main(warnings='ignore');