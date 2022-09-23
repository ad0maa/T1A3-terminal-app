menu = {
    'Chips': 4.50,
    'Nuggets' : 7.00,
    'Burger' : 10.50,
    'Soda' : 2.00
}

order_items = []
total_price = 0
delivery = False


def print_menu():
    print('Today\'s menu: ')
    i = 1
    for food, price in menu.items():
        # i = food[i]
        print (f'{i}.', food, '- $',price)
        i += 1


def order_food():
    print('\nWhat would you like to order today?')
    global order_items, total_price

    while True:
        order_req = int(input())
        if order_req == 1:
            sub_total = menu[order_req]
            total_price += sub_total
            print(sub_total)
            print(total)

    #     elif option == 2:
    #         order_food()
    #     elif option == 3:       
    #         pickup_delivery()
    #         print_receipt()
    #         file_receipt()
    #         ready_time()
    #     elif option == 4:
    #         order_items = []
    #         total_price = 0
    #         delivery = False
    #     else:
    #         print('Invalid option')



    # while True:
    #     order_req = input()
    #     if order_req in menu:
    #         sub_total = menu[order_req]
    #         total_price += sub_total
    #         order_items.append([order_req, sub_total])
    #         # order_items.update({order_req : sub_total})
    #         while True:
    #             x = input('Would you like to \n[1] Add more items to order \n[2] Display Current Order \n[3] Back to Menu ')
    #             if x == '1':
    #                 print('What would you like to order next? ')
    #                 break
    #             elif x == '2':
    #                 print(f'You have ordered {order_items}.')
    #                 print(f'Your current total is ${total_price}.')
    #                 continue
    #             else:
    #                 clearing.clear()
    #                 return total_price


print_menu()
order_food()