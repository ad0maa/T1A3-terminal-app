class Customer:

    def __init__(self, first_name, last_name,phone ):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone

class Delivery(Customer):

    def __init__(self, first_name, last_name, phone, address):
        super().__init__(first_name, last_name, phone)
        self.address = address