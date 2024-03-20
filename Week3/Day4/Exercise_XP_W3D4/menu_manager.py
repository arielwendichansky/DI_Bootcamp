import psycopg2


HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = '636231'
DATABASE = 'Exercise_XP_W3D4'

class MenuManager:
    @classmethod
    def get_by_name(cls,name):
        try:
            connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
            c = connection.cursor()
            c.execute(f"SELECT item_name, item_price FROM menu_items WHERE item_name ='{name}'")
            connection.commit()
            item = c.fetchone()
            if item:
                return item
        except psycopg2.Error as e:
            print("Error saving menu item:", e)
            return None
        finally:
            connection.close()


    @classmethod
    def all_items (cls):
        try:
            connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
            c = connection.cursor()
            c.execute(f"SELECT item_name, item_price FROM menu_items")
            connection.commit()
            item = c.fetchall()
            if item:
                return item
        except psycopg2.Error as e:
            print("Error saving menu item:", e)
            return None
        finally:
            connection.close()


