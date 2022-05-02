from selenium.webdriver.common.keys import Keys
from unittest import skip
from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):
  def test_cannot_add_empty_list_items(self):
    #Marcos accidentally tries to submit an empty list item.
    #he hits enter on the empty input box

    #The home page refreshes, and there is an error message saying
    #that lists items cannot be blank

    #He tries again with some text and it works

    #Perversaly, he now decides to submit a second blank list item

    #He receives a similar warning on the list page

    #And he can correct it by filling some text in
    self.fail('write me!')
