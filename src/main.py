
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

# Take users order, add to variable 'receipt'

# Ask user if they want to order something else?

# Repeat above steps until user has finished ordering

order_items = {}
total_price = 0

def order_food(order_items, total_price):
    while True:
        print('What would you like to order today?')
        order_req = input()
        if order_req in menu:
            sub_total = menu[order_req]
            total_price = total_price + sub_total
            order_items.update({order_req : sub_total})
            print(f'Your order price is ${total_price}.')
            print(f'Your order items are {order_items}.')
            if input("Would you like to order anything else? [y/n]") != 'y':
                return total_price
    



# Ask if Delivery, add delivery fee to the order

def pickup_delivery(total_price):
    x = input('Is your order delivery or pickup?')
    if x == 'delivery':
        total_price = total_price + 7.50
        print(f'Your total including delivery is ${total_price}')
        return
    else: print(f'Your total is ${total_price}')



# Produce a receipt and output receipt to a text file

def gen_receipt():
    receipt = []
    for element in order_items:
        if element in str(total_price):
            receipt.append(element)
            print(receipt)
    print(str(order_items) + str(total_price))


for entry, amount in order_items:
    product = order_items.get(entry)

    print(f"{key} - {amount}x {name} - ${price}".format(key=entry, amount=amount, name=product['name'], price=product['price']))
print(f"Total price is {} \n".format(subtotal))

# Ask 

# Exit Application


# EXTRAS ONCE BASIC PROGRAM IS RUNNING

# Using datetime, give an estimate of when the order will be ready or delivered

# Show what has been ordered so far, with sub-total price

# Ask user if they have allergies, only display items that are appropriate to the user

# Ask if user is a member and apply discount price to the receipt


print_menu()
total_price = order_food(order_items, total_price)
pickup_delivery(total_price)
gen_receipt()