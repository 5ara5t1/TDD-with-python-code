# Utilizing pytest_django

from pytest_django.asserts import assertContains, assertTemplateUsed


def test_uses_home_template(client):
    response = client.get("/")
    assertTemplateUsed(response, "home.html")

# Smoke Test - Verify we have the right content in the template
def test_renders_home_content(client):
    response = client.get("/")
    assertContains(response, "To-Do")