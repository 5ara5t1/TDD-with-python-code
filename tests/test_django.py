from selenium import webdriver

class NewVisitorTest():
    def setup(self):
        browser = webdriver.Firefox()
    def teardown(self):
        self.browser.quit()
    
    def test_can_start_a_todo_list(self):
        # Edith has heard about a cool new online todo app
        # She goes to the browser to view the homepage
        self.browser.get("http://localhost:8000/?")

        # She notices that the page title mentions todo lists
        assert "To-Do" in browser.title

        # She is invited to enter a to-do item straight away
        assert "Fail the test" is 0