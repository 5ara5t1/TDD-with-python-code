import pytest
from selenium import webdriver
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

# using plain functions for testing, using liver server fixture
def test_can_start_a_todo_list(live_server, browser):
    # Edith has heard about a cool new online todo app
    # She goes to the browser to view the homepage
    browser.get(live_server.url)

    # She notices that the page title mentions todo lists
    assert "To-Do" in browser.title
