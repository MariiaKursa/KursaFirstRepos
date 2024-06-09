from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select



class SignUpSalesforce(BasePage):
    URL = "https://www.salesforce.com/eu/form/demo/overview-demo/?d=pb"

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(SignUpSalesforce.URL)

    def enter_contact_data(
        self, first_name, last_name, job_title, email, company, phone
    ):
        # Заповняємо текстові поля
        name_field = self.driver.find_element(By.NAME, "UserFirstName")
        name_field.send_keys(first_name)

        last_name_field = self.driver.find_element(By.NAME, "UserLastName")
        last_name_field.send_keys(last_name)

        job_title_field = self.driver.find_element(By.NAME, "UserTitle")
        job_title_field.send_keys(job_title)

        email_field = self.driver.find_element(By.NAME, "UserEmail")
        email_field.send_keys(email)

        company_field = self.driver.find_element(By.NAME, "CompanyName")
        company_field.send_keys(company)

        phone_field = self.driver.find_element(By.NAME, "UserPhone")
        phone_field.send_keys(phone)

    # Використання команди Select для вибору зі списку
    def select_employess(self):
        count_of_employess = self.driver.find_element(By.NAME, "CompanyEmployees")
        select = Select(count_of_employess)
        select.select_by_value("10")

    def select_country(self):
        country = self.driver.find_element(By.NAME, "CompanyCountry")
        select_country = Select(country)
        select_country.select_by_visible_text("Ukraine")
