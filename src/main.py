
# Welcome Message
from ast import For
from datetime import datetime, date, timedelta
from prettytable import PrettyTable
# import clearing


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

# clearing.clear()
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
    print('Today\'s menu is: ')
    for food, price in menu.items():
        print (food, '- $',price)

# Ask 'Are you ready to order?'

# Take users order, add to variable 'receipt'

# Ask user if they want to order something else?

# Repeat above steps until user has finished ordering

order_items = []
total_price = 0
delivery = False

def order_food(order_items, total_price):
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
                return total_price


# Ask if Delivery, add delivery fee to the order



def pickup_delivery():
    global total_price, delivery
    x = input('Is your order delivery or pickup?')
    if x == 'delivery':
        total_price += 7.50
        print('$7.50 delivery fee has been added to your order.')
        print(f'Your total including delivery is ${total_price}')
        delivery = True

    else: print(f'Your total is ${total_price}')


# print(delivery)

# Produce a receipt and output receipt to a text file

def print_receipt():
    global table 
    table = PrettyTable(['Item', 'Price'])
    for food,price in order_items:
        table.add_row([food,'$' + str(price)])
    table.add_row(['-'* 8,'-' * 8])
    if delivery is True:
        table.add_row(['DELIVERY', '$7.50'])
        table.add_row(['-'* 8,'-' * 8])
        table.add_row(['TOTAL', '$' + str(total_price) ])

    else:
        table.add_row(['TOTAL', '$' + str(total_price)])
    print(table)
    print('Your total bill amount is $', total_price)
    return

# today = date.today()

def file_receipt():
    with open('receipt.txt', 'w') as f:
        f.write('McFoo Receipt\n')
        f.write('Order Placed: '+ datetime.now().strftime('%B %d, %Y %H:%M:%S') + '\n')
        f.write(str(table))
        f.write('\nThank you for your order!')
        f.write('\nMcFoo Restaurants Australia')


# Ask 

# Exit Application

# EXTRAS ONCE BASIC PROGRAM IS RUNNING

# Using datetime, give an estimate of when the order will be ready or delivered

def ready_time():
    now = datetime.now()
    pickup_time = now + timedelta(minutes=20)
    delivery_time = now + timedelta(minutes=40)
    print('Order placed at ', now.strftime("%H:%M %d %B %Y"))
    if delivery == True:
        print('Your order will be delivered at approximately', delivery_time.strftime("%H:%M %d %B %Y"))
    else:
        print('Your order will be ready for pickup at', pickup_time.strftime("%H:%M %d %B %Y"))


# Show what has been ordered so far, with sub-total price

# Ask user if they have allergies, only display items that are appropriate to the user

# Ask if user is a member and apply discount price to the receipt

# gen_receipt()

if __name__ == '__main__':
    print_menu()
    total_price = order_food(order_items, total_price)
    pickup_delivery()
    print_receipt()
    file_receipt()
    ready_time()

