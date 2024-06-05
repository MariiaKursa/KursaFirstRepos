from modules.ui.page_objects.sign_in_page import SignInPage
import pytest

@pytest.mark.ui
def test_check_incorrect_username_page_object():
    #створення об'єкту сторінки
    sign_in_page = SignInPage()

    #відкриваємо сторінку
    sign_in_page.go_to()

    #виконуємо спробу увійти
    sign_in_page.try_login('page@jgmail.com', 'wrong pass')

    #перевіряємо заголовок сторінки
    assert sign_in_page.check_title('Sign in to GitHub · GitHub')

    #Закриваємо браузер
    sign_in_page.close()