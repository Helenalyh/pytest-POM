from selenium.webdriver.common.by import By
from .base_element import BaseElement
from .base_page import BasePage
from .locator import Locator

class AmazonPage(BasePage):
    url = 'https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&'

    @property
    def emailInput(self):
        return self.base_element_by_id('ap_email')
    
    @property
    def contiButton(self):
        return self.base_element_by_id('continue')
    
    @property
    def pwdInput(self):
        return self.base_element_by_id('ap_password')

    @property
    def signInButton(self):
        return self.base_element_by_id('signInSubmit')
