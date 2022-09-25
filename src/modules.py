import main
from datetime import datetime, date, timedelta
from prettytable import PrettyTable
# import clearing

#Variable Declarations:

#food menu

order_items = []
total_price = 0
delivery = False

# Splash Screen for Application

def splash():
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


def get_input(prompt):
    while True:
        i = (input(prompt))
        # if len(i) == 1 and i.isdigit():
        if i.isdigit():
            return int(i)
        else:
            print('Invalid input, please enter a menu item number. (Eg - \'1\')')

            
        # except Exception:
        #     print('Invalid input, please enter a menu item number. (Eg - \'1\')')


        # else:
        #     if i > 10:
        #         # break
        #         return i

# Main Menu Function

def menu_display():
    print('\n[1] View Menu')
    print('[2] Make an Order')
    print('[3] View Current Order')
    print('[4] Finalize Order')
    print('[5] Clear Order')
    print('[0] Quit Application')

def main_menu():
    menu_display()
    option = get_input('Enter your selection: ')
    while option != 0:
        if option == 1:
            print_menu()
        elif option == 2:
            new_order()
        elif option == 3:
            view_order()
        elif option == 4:       
            pickup_delivery()
            print_receipt()
            file_receipt()
            ready_time()
        elif option == 5:
            clear_order()
        elif option == 0:
            break
        else:
            print('Invalid input, please enter a menu item number. (Eg - \'1\')')
        menu_display()
        option = get_input('Enter your selection: ')

# Print menu items

def print_menu():
    print('\nToday\'s menu: ')
    i = 1
    for food, price in main.menu.items():
        # i = food[i]
        print (f'{i}.', food, '- $',price)
        i += 1
    # print('\n')

# Pickup or delivery function

def pickup_delivery():
    global total_price, delivery
    x = get_input('Please select [1] for Delivery or [2] for Pickup. ')
    if x == 1:
        total_price += 7.50
        print('$7.50 delivery fee has been added to your order.')
        print(f'Your total including delivery is ${total_price}')
        delivery = True
    # elif x == 2:



# Order placing function

def new_order():
    print('\nWhat would you like to order today?')
    global order_items, total_price
    while True:
        order_req = get_input('Enter your selection: ') - 1
        if order_req < len(main.menu):
            for index, (key, value) in enumerate(main.menu.items()):
                if index == order_req:
                    sub_total = value
                    total_price += sub_total
                    order_items.append([key, sub_total])
                    print(f'\n{key} added to order.\n')
                    while True:
                        x = input('\nWould you like to:\n[1] Add more items to order \n[2] Display current order \n[3] Display Food Menu \n[4] Back to Main Menu ')
                        if x == '1':
                            print('What would you like to order next? ')
                            break
                        elif x == '2':
                            view_order()
                            continue
                        elif x == '3':
                            print_menu()
                            continue
                        else:
                            print('Invalid input, please enter a menu item number. (Eg - \'1\')')
                            return total_price
        else:
            print('Entry not on Menu, please select a valid menu item number. ')


# Display Current Order
def view_order():
    if len(order_items) == 0:
        print('\nYou have no items in your order.\n')
    else:
        print('\nYou have ordered:\n')
        for food, price in order_items:
            print(food + ' $' + str(price))
        print(f'Your current total is ${total_price}\n')

# Clear current order

def clear_order():
    global order_items, total_price, delivery
    order_items = []
    total_price = 0
    delivery = False
    print('\nOrder cleared\n')


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


# Save Receipt to file


def file_receipt():
    print('Would you like to store your receipt in a file? \n[1] Yes [2] No')
    x = get_input(' ')
    if x == 1:
        with open('receipt.txt', 'w') as f:
            f.write('McFoo Receipt\n')
            f.write('Order Placed: '+ datetime.now().strftime('%B %d, %Y %H:%M:%S') + '\n')
            f.write(str(table))
            f.write('\nThank you for your order!')
            f.write('\nMcFoo Restaurants Australia')
            print('\nYour receipt has been saved as receipt.txt')


# Using datetime, give an estimate of when the order will be ready or delivered

def ready_time():
    now = datetime.now()
    pickup_time = now + timedelta(minutes=20)
    delivery_time = now + timedelta(minutes=40)
    print('Order placed at ', now.strftime("%H:%M, %d %B %Y"))
    if delivery == True:
        print('Your order will be delivered at approximately', delivery_time.strftime("%H:%M, %d %B %Y\n"))
    else:
        print('Your order will be ready for pickup at', pickup_time.strftime("%H:%M, %d %B %Y\n"))