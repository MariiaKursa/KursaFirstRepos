from modules.ui.page_objects.search_and_select_page import SearchAndSelectPage
from modules.ui.page_objects.rozetka_tracking_page import TrackingPage
import pytest


@pytest.mark.rztk_ui
def test_search_and_select_page():

    search_and_select_page = SearchAndSelectPage()

    search_and_select_page.go_to()

    search_and_select_page.input_products_for_search_box("басейн")

    search_and_select_page.select_product

    search_and_select_page.close


@pytest.mark.rztk_ui
def test_tracking_page():

    rozetka_tracking_page = TrackingPage()

    rozetka_tracking_page.go_to()

    rozetka_tracking_page.tracking(8765434567)

    rozetka_tracking_page.close()
