#Import
import menuitems 
import clearing
#clearing.clear()

# Variables
order_type = ''

# Splash screen
print("Hello and Welcome to our Japanese Restaurant")


# CIL Menu



# Get user input on if order is pickup or delivery (build object based on answers)

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


# WORKING CODE HERE
# ordertype()
# print(order_type)
print(menuitems.cali_roll.__dict__)



# Ask User what part of the menu they would like to display (Entree, Main, Dessert, Drinks)

# Ask user if they have allergies, only display items that are appropriate to the user

# Display the menu to user and ask them if they'd like to order something from this menu

# Add menu items to order object

# Ask user if they want to order something else?

# Repeat above steps until user has finished ordering

# If Delivery, add delivery fee to the order

# Produce a receipt and output receipt to a text file

# Using datetime, give an estimate of when the order will be ready or delivered

