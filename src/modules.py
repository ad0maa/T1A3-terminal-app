# Import
from datetime import datetime, date, timedelta
import main
from prettytable import PrettyTable
import clearing

#Variable Declarations:
order_items = []
total_price = 0
delivery = False

# Splash Screen for Application
def splash():
    """
    This function prints out the application splash screen art when application is launched
    """    
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
    print(input('Press Enter to continue'))

# Input Validation

def get_input(prompt):
    """_This function validates that users have input a valid integer and displays an error message if input is incorrect_

    Args:
        prompt (_str_): _Allows the function to be reused with different prompts throughout application_

    Returns:
        _int_: _returns the users input as a valid integer_
    """    
    while True:
        i = (input(prompt))
        if i.isdigit():
            return int(i)
        else:
            print('Invalid input, please enter a menu item number. (Eg - \'1\')')

# Main Menu Function

def menu_display():
    """_Prints out strings that form the main menu_
    """    
    print('\n[1] View Food Menu')
    print('[2] Place an Order')
    print('[3] View Current Order')
    print('[4] Finalize Order')
    print('[5] Clear Order')
    print('[0] Quit Application')

def main_menu():
    """_Main menu and flow of application_
    """    
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

# Print food menu items

def print_menu():
    """_Prints out the food menu to the terminal_
    """    
    clearing.clear()
    print('Today\'s menu: ')
    i = 1
    for food, price in main.menu.items():
        print (f'{i}.', food, '- $',price)
        i += 1

# Pickup or delivery function

def pickup_delivery():
    """_User inputs whether their order is pickup or delivery_
    _returns True boolean value to delivery for use in other functions._
    _updates total price with delivery added if applicable_
    """    
    global total_price, delivery
    x = get_input('Please select [1] for Delivery or [2] for Pickup. ')
    while True:
        if x == 1:
            total_price += 7.50
            print('\n$7.50 delivery fee has been added to your order.')
            print(f'Your total including delivery is ${total_price}')
            delivery = True
            break
        elif x ==2:
            break
        else:
            print('Invalid input, please enter [1] for Delivery or [2] for Pickup.')

# Order placing function

def new_order():
    """_Function to add food menu items to order_items variable_
    _updates total_price when items are added_

    Returns:
        _float_: _total_price_
    """    
    print('\nPlease enter the menu item number of the food you wish to add to your order: ')
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
                        elif x == '4':
                            return total_price
                        else:
                            print('Invalid input, please enter a menu item number. (Eg - \'1\')')
        else:
            print('Entry not on Menu, please select a valid menu item number. ')


# Display Current Order
def view_order():
    """_Used to display what items have been added to order during use of application_
    """    
    if len(order_items) == 0:
        print('\nYou have no items in your order.\n')
    else:
        print('\nYou have ordered:\n')
        for food, price in order_items:
            print(food + ' $' + str(price))
        print(f'Your current total is ${total_price}\n')

# Clear current order

def clear_order():
    """_Used to clear current order_
    """
    clearing.clear()
    global order_items, total_price, delivery
    order_items = []
    total_price = 0
    delivery = False
    print('Order cleared\n')


# Produce a receipt and output receipt to a text file

def print_receipt():
    """_function to print receipt to terminal_
    _different receipt is printed depending if delivery was selected_
    """    
    global table 
    table = PrettyTable(['Item', 'Price'])
    clearing.clear()
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
    return


# Save Receipt to file

def file_receipt():
    """_function to save the receipt to a text file_
    """    
    print('Would you like to store your receipt in a file? \n[1] Yes [2] No ')
    x = get_input('')
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
    """_used to print pickup or delivery time to the terminal_
    """    
    now = datetime.now()
    pickup_time = now + timedelta(minutes=20)
    delivery_time = now + timedelta(minutes=40)
    print('Order placed at ', now.strftime("%H:%M, %d %B %Y"))
    if delivery == True:
        print('Your order will be delivered at approximately', delivery_time.strftime("%H:%M, %d %B %Y\n"))
    else:
        print('Your order will be ready for pickup at', pickup_time.strftime("%H:%M, %d %B %Y\n"))