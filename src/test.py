def file_receipt():
    print('Would you like to store your receipt in a file? \n[1] Yes [2] No')
    x = input()
    if x == 1:
        with open('receipt.txt', 'w') as f:
            f.write('McFoo Receipt\n')
            # f.write('Order Placed: '+ datetime.now().strftime('%B %d, %Y %H:%M:%S') + '\n')
            # f.write(str(table))
            f.write('\nThank you for your order!')
            f.write('\nMcFoo Restaurants Australia')

file_receipt()