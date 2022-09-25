# Import
import modules

# Food Menu Dictionary
menu = {
    'Chips': 4.50,
    'Nuggets' : 7.00,
    'Jalapeno Poppers' : 8.00,
    'Chicken Burger' : 10.50,
    'Cheeseburger' : 8,
    'Double Cheeseburger' : 11.50,
    'Coke' : 2.00,
    'Sprite' : 2.00,
    'Fanta' : 2.00,
    'Water' : 1.50,
}

if __name__ == '__main__':
    modules.splash()
    print('Hello and Welcome to Mcfoo\'s Ordering System')
    print('How can we help you today?\n')
    modules.main_menu()
    print("Thank you for choosing McFoo for your calorie fix today!")