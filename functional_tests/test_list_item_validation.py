from selenium.webdriver.common.keys import Keys
from unittest import skip
from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):
  def get_error_element(self):
    return self.browser.find_element_by_css_selector('.has-error')

  def test_cannot_add_empty_list_items(self):
    #Marcos accidentally tries to submit an empty list item.
    #he hits enter on the empty input box
    self.browser.get(self.live_server_url)
    self.get_item_input_box().send_keys(Keys.ENTER)

    #The home page refreshes, and there is an error message saying
    #that lists items cannot be blank
    self.wait_for(lambda: self.browser.find_element_by_css_selector(
      '#id_text:invalid'
    ))
    
    #He tries again with some text and it works
    self.get_item_input_box().send_keys('Buy milk')
    self.wait_for(lambda: self.browser.find_element_by_css_selector(
      '#id_text:valid'
    ))

    self.get_item_input_box().send_keys(Keys.ENTER)
    self.wait_for_row_in_list_table('1: Buy milk')

    #Perversaly, he now decides to submit a second blank list item
    self.get_item_input_box().send_keys(Keys.ENTER)
    
    #He receives a similar warning on the list page
    self.wait_for(lambda: self.browser.find_element_by_css_selector(
      '#id_text:invalid'
    ))
    

    #And he can correct it by filling some text in
    self.get_item_input_box().send_keys('Buy tea')
    self.get_item_input_box().send_keys(Keys.ENTER)
    self.wait_for_row_in_list_table('1: Buy milk')
    self.wait_for_row_in_list_table('2: Buy tea')

  def test_cannot_add_duplicated_list_items(self):
    #Marcos now go to the home page and add a new list item
    self.browser.get(self.live_server_url)
    self.get_item_input_box().send_keys('Apply for a job')
    self.get_item_input_box().send_keys(Keys.ENTER)
    self.wait_for_row_in_list_table('1: Apply for a job')

    #He tries to enter a duplicate item
    self.get_item_input_box().send_keys('Apply for a job')
    self.get_item_input_box().send_keys(Keys.ENTER)

    #He sees a helpful error message
    self.wait_for(lambda: self.assertEqual(
      self.get_error_element().text,
      "You've already got this item in your list"
    ))
    
  def test_error_messages_are_cleared_on_input(self):
    # Marcos starts a list and causes a validation error
    self.browser.get(self.live_server_url)
    self.get_item_input_box().send_keys('Its duplicated')
    self.get_item_input_box().send_keys(Keys.ENTER)
    self.wait_for_row_in_list_table('1: Its duplicated')
    self.get_item_input_box().send_keys('Its duplicated')
    self.get_item_input_box().send_keys(Keys.ENTER)

    self.wait_for(lambda: self.assertTrue(
      self.get_error_element().is_displayed()
    ))

    # He starts typing in the input box to clear the error
    self.get_item_input_box().send_keys('a')

    # He is pleased to see that the error messag disappears
    self.wait_for(lambda: self.assertFalse(
      self.get_error_element().is_displayed()
    ))