from menu_item import MenuItem
from menu_manager import MenuManager

def show_user_menu():
    while True:
        answ = input("Hi! Choose an option:\n> View an Item (V)\n> Add an Item (A)\n> Delete an Item (D)\n> Update an Item (U)\n> Show the Menu (S)\n> To leave (X)\n>>> ")
        if answ.upper() == 'V':
            brsw_food = input("What dish you are looking for? ")
            dish = MenuManager()
            print(dish.get_by_name(brsw_food))
        if answ.upper() == 'A':
            add_item_to_menu()
        if answ.upper() == 'D':
            remove_item_from_menu()
        if answ.upper() == 'U':
            update_item_from_menu()
        if answ.upper() == 'S':
            all = MenuManager()
            print(all.all_items())
        if answ.upper() == 'X':
            all = MenuManager()
            print(all.all_items())
            break



def add_item_to_menu():
    name = input("What food you want to add to the menu?\n>>> ")
    price = input("Which price you want to give to this new dish?\n>>> ")
    new_dish = MenuItem(name, price)
    new_dish.save()


def remove_item_from_menu():
    name = input("What dish you want to add to the menu?\n>>> ")
    drop_dish = MenuItem(name)
    drop_dish.delete(name)

def update_item_from_menu():
    old_name = input("What dish you want to update from the menu?\n>>> ")
    old_price = input("What is the current price?\n>>> ")
    name = input("Which is the new dish?\n>>> ")
    price = input("Which price you want to give to this (Enter for no changes)?\n>>> ")
    update_dish = MenuItem(old_name.title(), old_price)
    update_dish.update(name.title(), price)

show_user_menu()
