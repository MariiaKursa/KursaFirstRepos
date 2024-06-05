import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


@pytest.mark.ui
def test_check_incorrect_username():
    #Створення об'єкту для керування браузером
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )

    #відкриваємо сторінку https://github.com/login
    driver.get('https://github.com/login')

    #Знаходимо поле, в яке будемо вводити неправильне ім'я
    login_elem = driver.find_element(By.ID, 'login_field')

    #Вводимо неправильне ім'я користувача або пошту
    login_elem.send_keys('sergiibutenko@mistakeinemail.com')
    

    #Знаходимо поле паролю
    log_password = driver.find_element(By.ID, 'password')

    #Вводимо неправильне ім'я користувача або пошту
    log_password.send_keys('123456')
    

    #Знаходимо кнопку
    btn_element = driver.find_element(By.NAME, 'commit')

    #Емулюємо клік
    btn_element.click()

    assert driver.title == 'Sign in to GitHub · GitHub'
    





    #закриваємо браузер
    driver.close()