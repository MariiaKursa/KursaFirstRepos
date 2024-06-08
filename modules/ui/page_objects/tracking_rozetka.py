from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys




class Tracking(BasePage):
    URL = "https://rozetka.com.ua/ua/tracking/"

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(Tracking.URL)
    
    def tracking(self, number):

        input_track_number = self.driver.find_element(By.ID, 'searchText')
        
        input_track_number.send_keys(number)

        input_track_number.send_keys(Keys.RETURN)

        btn_track = self.driver.find_element(By.XPATH, '/html/body/rz-app-root/div/div/rz-tracking/div/div/form/fieldset/div/div/button')

        btn_track.click

        


   

    

    
