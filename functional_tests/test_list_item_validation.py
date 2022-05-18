from selenium.webdriver.common.keys import Keys
from unittest import skip
from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):
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
