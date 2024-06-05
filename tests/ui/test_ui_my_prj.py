from modules.ui.page_objects.search_and_order import Search_and_Order
import pytest


@pytest.mark.rozetka_ui
def test_search_and_order():

    search_and_order = Search_and_Order()

    search_and_order.go_to()
   