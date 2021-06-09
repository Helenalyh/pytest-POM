from selenium.webdriver.common.by import By
from .base_element import BaseElement
from .base_element import Cast
from .base_page import BasePage
from .locator import Locator

class IMDbPage(BasePage):

    url = 'https://www.imdb.com/title/tt0097165/'

    @property
    def cast(self):
        locator = Locator(by=By.CLASS_NAME, value='cast_list')
        return Cast(self.driver, locator)
