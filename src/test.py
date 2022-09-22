# order_total = 10.00

# def add_delivery_fee(order):
#     order = order + 7.50
#     return order

# order_total = add_delivery_fee(order_total)

# print(order_total)
from prettytable import PrettyTable


table = PrettyTable(['Item', 'Price ($)'])
total = 0


# order_items = (['Soda', 2],['Burger', 10])
total_price = 17.50


order_items = {'Soda': 2, 'Burger': 10}
for k,v in order_items.items():
    table.add_row([k,v])

table.add_row(['-'* 8,'-' * 8])
table.add_row(['TOTAL', total_price])
print(table)
print('Your total bill amount is ', total_price, '/-')





# def gen_receipt():
#     # receipt = []
#     # for element in order_items:
#     #     if element in str(total_price):
#     #         receipt.append(element)
#     #         print(receipt)

#     for key, value in order_items.items():
#         print(key)
#         print(value)
#     print(str(order_items) + str(total_price))

# gen_receipt()