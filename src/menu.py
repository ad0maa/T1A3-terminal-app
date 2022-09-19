class Menu:
    
    def __init__(self, name, price, description, category):
        self.name = name
        self.price = price
        self.description = description
        self.category = category

class Drink(Menu):

    def __init__(self, name, price, description, category, volume, alc_percent):
        super().__init__(name, price, description, category)
        self.volume = volume
        self.alc_percent = alc_percent

class Food(Menu):

    def __init__(self, name, price, description, category, serve_size):
        super().__init__(name, price, description, category)
        self.serve_size = serve_size