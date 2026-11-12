# Utilizing pytest_django

from pytest_django.asserts import assertContains


def test_home_page_returns_correct_html(client):
    response = client.get("/")
    assertContains(response, "<title>To-Do</title>")
    assertContains(response, "<html>")
    assertContains(response, "</html>")