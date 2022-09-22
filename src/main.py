
# Welcome Message
from ast import For
from datetime import datetime, date
from prettytable import PrettyTable
import clearing


print('''
  __  __        ______                        
 |  \/  |      |  ____|                       
 | \  / |  ___ | |__  ___    ___              
 | |\/| | / __||  __|/ _ \  / _ \             
 | |  | || (__ | |  | (_) || (_) |            
 |_|__|_| \___||_| _ \___/  \___/             
 |  __ \       | |(_)                         
 | |  | |  ___ | | _ __   __ ___  _ __  _   _ 
 | |  | | / _ \| || |\ \ / // _ \| '__|| | | |
 | |__| ||  __/| || | \ V /|  __/| |   | |_| |
 |___/\/  \___||_||_|  \_/  \___||_|    \__, |
    /  \    _ __   _ __                  __/ |
   / /\ \  | '_ \ | '_ \                |___/ 
  / ____ \ | |_) || |_) |                     
 /_/    \_\| .__/ | .__/                      
           | |    | |                         
           |_|    |_|                         
\n\n''')
print(input('Press any key to continue'))
print('Hello and Welcome to McDoogals\n')

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
        print (food, '- $',price)

# Ask 'Are you ready to order?'

# Take users order, add to variable 'receipt'

# Ask user if they want to order something else?

# Repeat above steps until user has finished ordering

order_items = {}
total_price = 0

def order_food(order_items, total_price):
    while True:
        print('\nWhat would you like to order today?')
        order_req = input()
        if order_req in menu:
            sub_total = menu[order_req]
            total_price += sub_total
            order_items.update({order_req : sub_total})
            print(f'Your order price is ${total_price}.')
            print(f'Your order items are {order_items}.')
            if input("Would you like to order anything else? [y/n]") != 'y':
                return total_price
    



# Ask if Delivery, add delivery fee to the order

def pickup_delivery(total_price):
    x = input('Is your order delivery or pickup?')
    if x == 'delivery':
        total_price += 7.50
        print('$7.50 delivery fee has been added to your order.')
        print(f'Your total including delivery is ${total_price}')
        delivery = True # THIS NEEDS TO WORK
        return delivery
    else: print(f'Your total is ${total_price}')
    return


# Produce a receipt and output receipt to a text file

delivery = False
clearing.clear()


def print_receipt():
    global table 
    table = PrettyTable(['Item', 'Price ($)'])
    for k,v in order_items.items():
        table.add_row([k,'$' + str(v)])
    table.add_row(['-'* 8,'-' * 8])
    if delivery == True:
        table.add_row(['DELIVERY', '$7.50'])
        table.add_row(['-'* 8,'-' * 8])
    table.add_row(['TOTAL', '$' + str(total_price)])
    print(table)
    print('Your total bill amount is $', total_price)
    return

today = date.today()

def file_receipt():
    with open('receipt.txt', 'w') as f:
        f.write('McFoo Receipt\n')
        f.write(f'Order Placed: {today.strftime("%B %d, %Y")}\n')
        f.write(str(table))


# Ask 

# Exit Application


# EXTRAS ONCE BASIC PROGRAM IS RUNNING

# Using datetime, give an estimate of when the order will be ready or delivered

# Show what has been ordered so far, with sub-total price

# Ask user if they have allergies, only display items that are appropriate to the user

# Ask if user is a member and apply discount price to the receipt



# gen_receipt()

print_menu()
total_price = order_food(order_items, total_price)
pickup_delivery(total_price)
print_receipt()
file_receipt()

now = datetime.now()
now.time()
print('Your order will be ready at ', now.time())