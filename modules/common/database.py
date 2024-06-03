import sqlite3


class Database():

    def __init__(self):
        self.connection = sqlite3.connect(r"C:/Users/Asus/KursaFirstRepos" + r"/become_qa_auto.db")
        self.cursor = self.connection.cursor()

    def test_connection(self):
        sqlite_select_Query = "SELECT sqlite_version();"
        self.cursor.execute(sqlite_select_Query)
        record = self.cursor.fetchall()
        print(f"Connected succesfully. SQlite Database Version is: {record}")

    def get_all_users(self):
        query = "SELECT name, address, city FROM customers"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def get_user_address_by_name(self, name):
        query = f"SELECT address, city, postalCode, country FROM customers WHERE name = '{name}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def update_product_qnt_by_id(self, product_id, qnt):
        query = f"UPDATE products SET quantity = {qnt} WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit() 
    
    def select_product_qnt_by_id(self, product_id):
        query = f"SELECT quantity FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def insert_product(self, product_id, name, description, qnt):
        query = f"INSERT OR REPLACE INTO products (id, name, description, quantity) \
            VALUES ({product_id}, '{name}', '{description}', {qnt})"
        self.cursor.execute(query)
        self.connection.commit() 
    
    def delete_product_by_id(self, product_id):
        query = f"DELETE FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()
    
    def get_detailed_orders(self):
        query = "SELECT orders.id, customers.name, products.name, \
            products.description, orders.order_date \
            FROM orders \
            JOIN customers ON orders.customer_id = customers.id \
            JOIN products ON orders.product_id = products.id"
        
        
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    
    def data_sorting(self):
        query = "SELECT id, name, description, quantity \
            FROM products \
            ORDER BY quantity DESC"
        
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def data_limit(self):
        query = "SELECT id, name, description, quantity \
            FROM products \
            ORDER BY quantity DESC \
            LIMIT 1"
        
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def count_function(self):
        query = "SELECT COUNT(id) \
            FROM products"
                 
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def type_of_data_not_null(self):
        query = "SELECT address, city, postalCode, country \
            FROM customers \
            WHERE address AND city AND postalCode IS NOT NULL"
        
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def insert_new_date(self, today):
        query = f"INSERT OR REPLACE INTO orders (order_date) \
            VALUES ('{today}')"
        self.cursor.execute(query)
        self.connection.commit() 
    
    def group_users_by_city_and_country(self):
        query = "SELECT name, address, city, postalCode, country \
            FROM customers \
            GROUP BY country, city \
            ORDER BY country, city"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
  