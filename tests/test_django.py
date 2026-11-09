from selenium import webdriver

def test_django_installed():
    browser = webdriver.Firefox()
    browser.get("http://localhost:8000")
    assert "Congratulations!" in browser.title
