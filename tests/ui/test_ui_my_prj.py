from modules.ui.page_objects.search_and_order import SearchAndOrder
import pytest


@pytest.mark.rozetka_ui
def test_search_and_order():

    search_and_order = SearchAndOrder()

    search_and_order.go_to()
   