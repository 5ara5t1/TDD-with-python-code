import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

# Using pytest fixtures
@pytest.fixture
def browser():
    options = Options()
    options.add_argument("-headless")
    browser = webdriver.Firefox(options=options)
    browser.set_window_size(1400,900)
    yield browser
    browser.quit()

# Helper function, find row in list table
def check_for_row_in_list_table(browser, row_text):
    table = browser.find_element(By.ID, "id_list_table")
    rows = table.find_elements(By.TAG_NAME, "tr")
    assert row_text in [row.text for row in rows]

# using plain functions for testing, using liver server fixture
def test_can_start_a_todo_list(live_server, browser):
    # Edith has heard about a cool new online todo app
    # She goes to the browser to view the homepage
    browser.get(live_server.url)

    # She notices that the page header and title both mention to-do lists
    assert "To-Do" in browser.title
    header = browser.find_element(By.TAG_NAME, "h1").text
    assert "To-Do" in header

    # She is invited to enter a to-do item straight away
    inputbox = browser.find_element(By.ID, "id_new_item")
    assert inputbox.get_attribute("placeholder") == "Enter a to-do item"

    # She types "Buy Peacock Feathers" into a text box
    # (Edith's hobby is tying fly fishing lures)
    inputbox.send_keys("Buy Peacock Feathers")


    # When she hits enter, the page updates and now the page lists
    # "1. Buy Peacock Feathers" as in item in a to-do list table
    inputbox.send_keys(Keys.ENTER)
    time.sleep(1)

    check_for_row_in_list_table(browser, "1. Buy Peacock Feathers")

    # There is still a text box inviting her to add another item
    # She enters "use peacock feathers to make fly"
    inputbox = browser.find_element(By.ID, "id_new_item")
    inputbox.send_keys("Use peacock feathers to make a fly")
    inputbox.send_keys(Keys.ENTER)
    time.sleep(1)

    # the page updates again, but now shows both items on her list
    check_for_row_in_list_table(browser, "2. Use peacock feathers to make a fly")
    check_for_row_in_list_table(browser, "1. Buy Peacock Feathers")

    # Certain her tool works, she goes to sleep
