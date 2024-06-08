from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class SearchAndSelect(BasePage):
    URL = "https://rozetka.com.ua/ua/search/"

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(SearchAndSelect.URL)

    def input_products_for_search_box(self, product_name):

        inpute_product = self.driver.find_element(By.NAME, "search")
        inpute_product.send_keys(product_name)

    def select_product(self):

        select = Select(self.driver.find_element(By.CLASS_NAME, "suggest-list"))
        select.select_by_index("1")
    
    def btn_search(self):
        btn = self.driver.find_element(By.XPATH, '/html/body/rz-app-root/div/div/rz-header/rz-main-header/header/div/div/div/rz-search-suggest/form/button')
        btn.click

  
