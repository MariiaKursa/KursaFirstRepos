from modules.ui.page_objects.salesforce_sign_up_page import SignUpSalesforcePage
import pytest


@pytest.mark.sale_ui
def test_sign_up_page():

    salesforce_sign_up_page = SignUpSalesforcePage()

    salesforce_sign_up_page.go_to()

    salesforce_sign_up_page.enter_contact_data(
        "Mariia", "Kursa", "student", "myemail", "company", "999"
    )

    salesforce_sign_up_page.select_employess

    salesforce_sign_up_page.select_country

    salesforce_sign_up_page.close
