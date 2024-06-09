from modules.ui.page_objects.sign_up_salesforce import SignUpSalesforce
import pytest


@pytest.mark.sale_ui
def test_sign_up_page():

    sign_up = SignUpSalesforce()

    sign_up.go_to()

    sign_up.enter_contact_data(
        "Mariia", "Kursa", "student", "myemail", "company", "999"
    )

    sign_up.select_employess

    sign_up.select_country

    sign_up.close
