# order_total = 10.00

# def add_delivery_fee(order):
#     order = order + 7.50
#     return order

# order_total = add_delivery_fee(order_total)

# print(order_total)


order_items = {'Soda': 2, 'Burger' : 10}
total_price = 17.50

for entry, amount in order_items.items():
    product = order_items.get(entry)

    print(f"{key} - {amount}x {name} - ${price}".format(key=entry, amount=amount, name=product['name'], price=product['price']))
print("Total price is {} \n".format(subtotal))