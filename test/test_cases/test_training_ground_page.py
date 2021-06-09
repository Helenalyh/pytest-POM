from pytest import mark
from test.page_objects.google_page import GooglePage
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

@mark.google
def test_training_page(chrome_driver):
    trng_page = GooglePage(driver=chrome_driver)
    trng_page.go()
    trng_page.searchBar.input_text('cauliflower')
    trng_page.searchBar.input_text(Keys.ENTER)
    

    trng_page.go()
    trng_page.searchBar.input_text('Interstellar')
    trng_page.searchBar.input_text(Keys.ENTER)
    trng_page.goto('wikipedia').click()

