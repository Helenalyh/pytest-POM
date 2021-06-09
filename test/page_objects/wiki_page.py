from .base_page import BasePage
from selenium.webdriver.common.by import By
from .base_element import BaseElement
from .locator import Locator

class WikiPage(BasePage):

    url = 'https://en.wikipedia.org/wiki/West_with_the_Night'

    @property
    def talkButton(self):
        locator = Locator(by=By.ID, value='ca-talk')
        xpath='//li[@id="ca-talk"]'
        return self.base_element_by_xpath(xpath)