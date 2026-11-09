from selenium import webdriver

# Setup browser - Firefox <3
browser = webdriver.Firefox()

# confirm that django is installed and is running
def test_django_installed_and_running():
    browser.get("http://localhost:8000")
    assert "Congratulations!" in browser.title

# Test Website Title
def test_todolist_homepage_title():
    expected_title = "To-Do"
    assert expected_title is browser.title 

# Test if users can add todo item right away

# Test if user can type into the text box

# Test if the user can add a todo list element