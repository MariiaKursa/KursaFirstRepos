from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

class SearchAndOrder(BasePage):
    URL = "https://rozetka.com.ua/search/"

    def __init__(self) -> None:
        super().__init__()
    
    def go_to(self):
        self.driver.get(SearchAndOrder.URL)
