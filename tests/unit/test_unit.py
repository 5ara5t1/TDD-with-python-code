# Utilizing pytest_django

from pytest_django.asserts import assertTemplateUsed, assertContains
from django.http import HttpRequest
from lists.views import home_page 


# Test Home page returns correct html
def test_home_page_returns_correct_html():
    request = HttpRequest()
    response = home_page(request)
    html = response.content.decode("utf8")
    assert "<title>To-Do</title>" in html
    assert html.startswith("<html>")
    assert html.endswith("</html>")