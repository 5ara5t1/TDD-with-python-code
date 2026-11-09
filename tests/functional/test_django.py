import pytest
from selenium import webdriver

# Using pytest fixtures
@pytest.fixture
def browser():
    browser = webdriver.Firefox()
    yield browser
    browser.quit()

# using plain functions for testing, using liver server fixture
def test_can_start_a_todo_list(live_server, browser):
    # Edith has heard about a cool new online todo app
    # She goes to the browser to view the homepage
    browser.get(live_server.url)

    # She notices that the page title mentions todo lists
    assert "To-Do" in browser.title

    # She is invited to enter a to-do item straight away
    pytest.fail("Finish the test")