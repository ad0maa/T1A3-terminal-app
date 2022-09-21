# order_total = 10.00

# def add_delivery_fee(order):
#     order = order + 7.50
#     return order

# order_total = add_delivery_fee(order_total)

# print(order_total)


order_items = ['Soda', 'Burger']
order_total = 17.50

def gen_receipt():
    receipt = []
    for element in order_items:
        if element in str(order_total):
            receipt.append(element)
            print(receipt)

gen_receipt()