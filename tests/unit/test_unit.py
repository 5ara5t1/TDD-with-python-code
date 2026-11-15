# Utilizing pytest_django
import pytest
from pytest_django.asserts import assertContains, assertTemplateUsed


@pytest.mark.django_db
def test_uses_home_template(client):
    response = client.get("/")
    assertTemplateUsed(response, "home.html")

# Test renders input form
@pytest.mark.django_db
def test_renders_input_form(client):
    response = client.get("/")
    assertContains(response, '<form method="POST">')
    assertContains(response, '<input name="item_text"')



