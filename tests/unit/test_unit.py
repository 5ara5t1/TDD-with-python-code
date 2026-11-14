# Utilizing pytest_django

from pytest_django.asserts import assertContains, assertTemplateUsed


def test_uses_home_template(client):
    response = client.get("/")
    assertTemplateUsed(response, "home.html")

# Test renders input form
def test_renders_imput_form(client):
    response = client.get("/")
    assertContains(response, '<form method="POST">')
    assertContains(response, '<input name="item_text"')

def test_can_save_a_POST_request(client):
    response = client.post("/", data={"item_text": "A new list item"})
    assertContains(response, "A new list item")