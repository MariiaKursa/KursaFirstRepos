from modules.ui.page_objects.my_project import MyProject
from selenium.webdriver.common.by import By

class Search_and_Order(MyProject):
    URL = "https://rozetka.com.ua/search/"

    def __init__(self) -> None:
        super().__init__()
    
    def go_to(self):
        self.driver.get(Search_and_Order.URL)
