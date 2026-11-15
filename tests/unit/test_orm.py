from lists.models import Item
from pytest_django.asserts import assertTemplateUsed, assertContains

import pytest


# ORM Testing
@pytest.mark.django_db
def test_saving_and_retrieving_items():
    first_item = Item()
    first_item.text = "The first (ever) list item"
    first_item.save()

    second_item = Item()
    second_item.text = "Item the second"
    second_item.save()

    saved_items = Item.objects.all()
    assert saved_items.count() == 2

    first_saved_item = saved_items[0]
    second_saved_item = saved_items[1]
    assert first_saved_item.text == "The first (ever) list item"
    assert second_saved_item.text == "Item the second"

@pytest.mark.django_db
def test_can_save_a_POST_request_to_the_database(client):
    response = client.post("/", data={"item_text": "A new list item"})

    assert Item.objects.count() == 1
    new_item = Item.objects.first()
    assert new_item.text == "A new list item"
    assertTemplateUsed(response, "home.html")


@pytest.mark.django_db
def test_can_save_a_POST_request(client):
    response = client.post("/", data={"item_text": "A new list item"})
    assertContains(response, "A new list item")
    assertTemplateUsed(response, "home.html")

@pytest.mark.django_db
def test_home_page_saves_items_only_when_necessary(client):
    response = client.get("/")
    assert Item.objects.count() == 0