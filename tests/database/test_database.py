import pytest
from modules.common.database import Database


@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_connection()


@pytest.mark.database
def test_check_all_users():
    db = Database()
    users = db.get_all_users()

    print(users)

@pytest.mark.database
def test_check_user_sergii():
    db = Database()
    user = db.get_user_address_by_name('Sergii')

    assert user[0][0] == 'Maydan Nezalezhnosti 1'
    assert user[0][1] == 'Kyiv'
    assert user[0][2] == '3127'
    assert user[0][3] == 'Ukraine'

@pytest.mark.database
def test_product_qnt_update():
    db = Database()
    db.update_product_qnt_by_id(1, 25)
    water_quantity = db.select_product_qnt_by_id(1)

    assert water_quantity[0][0] == 25

@pytest.mark.database
def test_product_insert():
    db = Database()
    db.insert_product(4, 'печиво', 'солодке', 30)
    water_quantity = db.select_product_qnt_by_id(4)

    assert water_quantity[0][0] == 30

@pytest.mark.database
def test_product_delete():
    db = Database()
    db.insert_product(99, 'тестові', 'дані', 999)
    db.delete_product_by_id(99)
    qnt = db.select_product_qnt_by_id(99)
   

    assert len(qnt) == 0

@pytest.mark.database
def test_detailed_orders():
    db = Database()
    orders = db.get_detailed_orders()
    print('Замовлення', orders)
      

    assert len(orders) == 1

    assert orders[0][0] == 1
    assert orders[0][1] == 'Sergii'
    assert orders[0][2] == 'солодка вода'    
    assert orders[0][3] == 'з цукром'

@pytest.mark.database
def test_data_sorting():
    db = Database()
    products = db.data_sorting()

    print(products)

@pytest.mark.database
def test_data_limit():
    db = Database()
    products = db.data_limit()

    assert len(products) == 1
    assert products[0][3] == 30

    print(products)

@pytest.mark.database
def test_count_function_by_products_id():
    db = Database()
    products = db.count_function()

    assert products[0][0] == 4

    print('кількість найменувань', products)


@pytest.mark.database
def test_type_of_data_not_null():
    db = Database()
    not_null_columns = db.type_of_data_not_null()

    print(not_null_columns)

@pytest.mark.database
def test_insert_new_date():
    db = Database()
    new_date = db.insert_new_date('сьогодні')
    

    print(new_date)

@pytest.mark.database
def test_group_customers_city_country():
    db = Database()
    group = db.group_users_by_city_and_country()
    

    print(group)


    



    

    

    

