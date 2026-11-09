# Utilizing pytest_django

from pytest_django.asserts import assertTemplateUsed, assertContains

# Creating a deliberately failing unit test
def test_failing_smoke_test(client):
    assert (1+1) is 1
