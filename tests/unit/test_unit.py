# Utilizing pytest_django

from pytest_django.asserts import assertContains, assertTemplateUsed


def test_home_page_returns_correct_html(client):
    response = client.get("/")
    assertTemplateUsed(response, "home.html")