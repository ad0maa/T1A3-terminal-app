
# Welcome Message
from ast import For


print('Hello and Welcome to McDoogals')

# Program Menu (Show Food menu, make an order, exit)

# Create food menu (dictionary)

menu = {
    'Chips': 4.50,
    'Nuggets' : 7.00,
    'Burger' : 10.50,
    'Soda' : 2.00
}

# Print out Food Menu
def print_menu():
    print('Here is today\'s menu: ')
    for food, price in menu.items():
        print (food + '- $' + str(price))

# Ask 'Are you ready to order?'

order_items = {}
order_total = 0

while True:
    print('What would you like to order today?')
    order_req = input()
    if order_req in menu:
        sub_total = menu[order_req]
        order_total = order_total + sub_total
        order_items.update({order_req : sub_total})
        print(f'Your order price is ${order_total}.')
        print(f'Your order items are {order_items}.')
        if input("Would you like to order anything else? [y/n]") != 'y':
            break

# Take users order, add to variable 'receipt'

# Ask user if they want to order something else?

# Repeat above steps until user has finished ordering

# Ask if Delivery, add delivery fee to the order

def add_delivery_fee(order):
    order = order + 7.50
    return order

x = input('Is your order delivery or pickup?')
if x == 'delivery':
    order_total = add_delivery_fee(order_total)
    print(f'Your total including delivery is ${order_total}')
else: print(f'Your total is ${order_total}')


# Produce a receipt and output receipt to a text file

def gen_receipt():
    receipt = []
    for element in order_items:
        if element in str(order_total):
            receipt.append(element)
            print(receipt)
    # print(str(order_items) + str(order_total))

gen_receipt()
# Ask 

# Exit Application


# EXTRAS ONCE BASIC PROGRAM IS RUNNING

# Using datetime, give an estimate of when the order will be ready or delivered

# Show what has been ordered so far, with sub-total price

# Ask user if they have allergies, only display items that are appropriate to the user

# Ask if user is a member and apply discount price to the receipt


# print_menu()
# order_form()