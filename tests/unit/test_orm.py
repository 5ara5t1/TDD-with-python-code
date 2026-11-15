import pytest
from pytest_django.asserts import assertContains, assertRedirects

from lists.models import Item


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
    client.post("/", data={"item_text": "A new list item"})

    assert Item.objects.count() == 1
    new_item = Item.objects.first()
    assert new_item.text == "A new list item"



@pytest.mark.django_db
def test_can_save_a_POST_request(client):
    client.post("/", data={"item_text": "A new list item"})
    assert Item.objects.count() == 1
    new_item = Item.objects.first()
    assert new_item.text == "A new list item"

@pytest.mark.django_db
def test_redirects_after_POST_request(client):
    response = client.post("/", data={"item_text": "A new list Item"})
    assertRedirects(response, "/")

@pytest.mark.django_db
def test_home_page_saves_items_only_when_necessary(client):
    client.get("/")
    assert Item.objects.count() == 0


@pytest.mark.django_db
def test_saves_all_list_items(client):
    Item.objects.create(text="Itemy 1")
    Item.objects.create(text="Itemy 2")

    response = client.get("/")

    assertContains(response, "Itemy 1")
    assertContains(response, "Itemy 2")