from selenium.webdriver.common.by import By
from .base_element import BaseElement
from .base_element import Image
from .base_page import BasePage
from .locator import Locator

class GooglePage(BasePage):

    url = 'http://www.google.com'


    def goto(self,substr):
        xpath='//h3[contains(text(),'+substr+')]'
        return self.base_element_by_xpath(xpath)

    def findImage(self,i):
        self.imageButton.click()
        locator = Locator(by=By.XPATH,value='//*[@id="islrg"]/div[1]/div['+str(i)+']/a[1]/div[1]/img')
        return Image(driver=self.driver,
                    locator=locator)
    
    @property
    def searchBar(self):
        xpath='//input[@name="q"]'
        return self.base_element_by_xpath(xpath)
    
    @property
    def imageButton(self):
        xpath='//a[@class="hide-focus-ring"]'
        return self.base_element_by_xpath(xpath)
    
