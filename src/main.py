# Import
from unicodedata import name
# import menuitems
# import menu
# import dicts
import clearing
import os
from simple_term_menu import TerminalMenu
import time
# clearing.clear()

# Variables
order_type = ''

# Dictionaries 
entrees = {
    'Karaage Chicken': 8,
    'Edamame': 6,
    'Beef Tataki': 10,
    'Pork Gyoza': 7,
    'Vegetarian Gyoza': 7,
    'Agedashi Todu': 8.5,
}


ramen = {
    'Tonkatsu Ramen': 17,
    'Spicy Pork Ramen': 18,
    'Chicken Ramen': 18,
    'Miso Ramen': 18,
    'Vegetarian Ramen':17
}

mains = {
    'Chicken Katsu Don': 18,
    'Beef Curry': 17,
    'Teriyaki Chicken': 15,
    'Mixed Bento Box': 18.5,
}

sushi = {
    'Cooked Tuna Roll': 5,
    'California Roll': 5,
    'Vegetarian Roll': 4,
    'Prawn Roll': 5,
    'Salmon Sashimi': 10,
}

drinks = {
    'Coca-Cola': 3,
    'Coca-Cola Zero': 3,
    'Sprite': 3,
    'Gingerbeer': 4,
    'Iced Tea': 4,
}


def print_menu(name):
    for k,v in name.items():
        print (k + ' $' + str(v))


# Splash screen
# print("Hello and Welcome to our Japanese Restaurant")


def ordertype():
    global order_type
    order_type = input("Would you like to order Pickup or Delivery?")
    if order_type.lower() == 'pickup':
        print('Pickup order selected')
        order_type = 'pickup'
        return order_type

    elif order_type.lower() == 'delivery':
        print('Delivery order selected')
        order_type = 'delivery'
        return order_type
    else:
        print("Please enter either 'pickup' or 'delivery'")

# CIL Menu


def main():
    print("Hello and Welcome to our Japanese Restaurant\n")
    main_menu_items = ["[1] Make an Order", "[2] View Entree Menu", "[3] View Ramen Menu",
                       "[4] View Main Menu", "[5] View Sushi menu", "[6] View Drinks Menu", "[0] Quit"]
    terminal_menu = TerminalMenu(main_menu_items)
    menu_entry_index = terminal_menu.show()
    # main_menu_exit = False

    print(f"You have selected {main_menu_items[menu_entry_index]}!")

    main_menu = TerminalMenu(
        menu_entries=main_menu_items,
        # title=main_menu_title,
        # clear_screen= True,
    )

    while not main_menu_exit:
        main_sel = main_menu.show()

        if main_sel == 0:
            print("You'd like to make an order!")
            ordertype()
            # time.sleep(2)
        elif main_sel == 1:
            print("Here is the Entree Menu")
            print(print_menu(entrees))
            # time.sleep(2)
        elif main_sel == 2:
            print("Here is the Ramen Menu")
            print(print_menu(ramen))
            # time.sleep(2)
        elif main_sel == 3:
            print("Here is the Main Menu")
            print(print_menu(mains))
            # time.sleep(2)
        elif main_sel == 4:
            print("Here is the Sushi Menu")
            print(print_menu(sushi))
            # time.sleep(2)
        elif main_sel == 5:
            print("Here is the Drinks Menu")
            print(print_menu(drinks))
            # time.sleep(2)
        elif main_sel == 6:
            main_menu_exit = True
            print("Quit Selected")


if __name__ == "__main__":
    main()

# Get user input on if order is pickup or delivery (build object based on answers)


# WORKING CODE HERE
# ordertype()
# print(order_type)
# print(menuitems.cali_roll.__dict__)

# Ask User what part of the menu they would like to display (Entree, Main, Dessert, Drinks)


# Ask user if they have allergies, only display items that are appropriate to the user

# Display the menu to user and ask them if they'd like to order something from this menu

# Add menu items to order object

# Ask user if they want to order something else?

# Repeat above steps until user has finished ordering

# If Delivery, add delivery fee to the order

# Produce a receipt and output receipt to a text file

# Using datetime, give an estimate of when the order will be ready or delivered
