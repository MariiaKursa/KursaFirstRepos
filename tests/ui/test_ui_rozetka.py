from modules.ui.page_objects.search_and_select import SearchAndSelect
from modules.ui.page_objects.tracking_rozetka import Tracking
import pytest


@pytest.mark.rztk_ui
def test_search_and_select():

    search_and_select = SearchAndSelect()

    search_and_select.go_to()

    search_and_select.input_products_for_search_box("басейн")

    search_and_select.select_product

    search_and_select.close


@pytest.mark.rztk_ui
def test_tracking():

    tracking_page = Tracking()

    tracking_page.go_to()

    tracking_page.tracking(8765434567)

    tracking_page.close()
