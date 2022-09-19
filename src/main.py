# Splash screen

# Get user input on if order is pickup or delivery (build object based on answers)

print("Hello and Welcome to Curries 'R Us!")
print(input.lower(('Are you wanting to order Takeaway or Delivery?')))
order_type = input().lower()

if order_type == 'pickup':
    print('Pickup order')
elif order_type == 'delivery':
    print('Delivery order')

# Ask User what part of the menu they would like to display (Entree, Main, Dessert, Drinks)

# Ask user if they have allergies, only display items that are appropriate to the user

# Display the menu to user and ask them if they'd like to order something from this menu

# Add menu items to order object

# Ask user if they want to order something else?

# Repeat above steps until user has finished ordering

# If Delivery, add delivery fee to the order

# Produce a receipt and output receipt to a text file

# Using datetime, give an estimate of when the order will be ready or delivered

