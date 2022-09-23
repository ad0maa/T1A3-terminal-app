from ast import For
from datetime import datetime, date
from prettytable import PrettyTable
import clearing


menu = {
    'Chips': 4.50,
    'Nuggets' : 7.00,
    'Burger' : 10.50,
    'Soda' : 2.00
}

order_items = []
total_price = 0
delivery = False



print('\nWhat would you like to order today?')

while True:
    order_req = input()
    if order_req in menu:
        sub_total = menu[order_req]
        total_price += sub_total
        order_items.append([order_req, sub_total])
        # order_items.update({order_req : sub_total})

        x = input('Would you like to [1] Order More? [2] Display Current Order? [3] Quit ')
        if x == '1':
            print('What would you like to order next? ')
            continue
        elif x == '2':
            print('Display Current Order')
            print(f'Your order price is ${total_price}.')
            print(f'Your order items are {order_items}.')
            continue
        else:
            break
            # return total_price
        # if input("Would you like to order anything else? [y/n]") != 'y':
        #     return total_price

print(order_items)