from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


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
        element = self.driver.find_element(By.XPATH, "//li[@data-name='басейн каркасний']")
        select = Select(element)
        select.select_by_index(3)
        select.select_by_visible_text('басейн дитячий')
        
    
    

 