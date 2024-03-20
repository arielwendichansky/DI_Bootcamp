import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = '636231'
DATABASE = 'Exercise_XP_W3D4'


class MenuItem:
        def __init__(self,name,price=None):
                self.name = name
                self.price = price

        def save(self):
                try:
                        connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
                        c = connection.cursor()
                        c.execute(f"INSERT INTO menu_items(item_name,item_price) VALUES ('{self.name}',{self.price})")
                        connection.commit()
                        print("Item was added successfully")
                except psycopg2.Error as e:
                        print("Error saving menu item:", e)
                finally:
                        connection.close()

        def delete(self,name):
                try:
                        connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
                        c = connection.cursor()
                        c.execute(f"DELETE FROM menu_items WHERE item_name ='{name}'")
                        connection.commit()
                        print("Item was deleted successfully")
                except psycopg2.Error as e:
                        print("Error saving menu item:", e)
                finally:
                        connection.close()

        def update(self, new_name=None, new_price=None):
                try:
                        connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
                        c = connection.cursor()
                        if new_name and new_price:
                                c.execute(f"UPDATE menu_items SET item_name = '{new_name}', item_price = {new_price} WHERE (item_name='{self.name}' AND item_price = {self.price})")
                                connection.commit()
                                print(f"{new_name} was updated successfully with the price {new_price}")
                        elif new_name:
                                c.execute(f"UPDATE menu_items SET item_name = '{new_name}' WHERE (item_name='{self.name}')")
                                connection.commit()
                                print(f"{new_name} was updated successfully ")
                        elif new_price is not None:
                                c.execute(f"UPDATE menu_items SET item_price = {new_price} WHERE (item_price = {self.price})")
                                connection.commit()
                                print(f"{new_price} was updated successfully")
                except psycopg2.Error as e:
                        print("Error saving menu item:", e)
                finally:
                        connection.close()










