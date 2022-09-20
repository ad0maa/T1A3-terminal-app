class Menu:
    
    def __init__(self, name, price, category, is_vege, gluten_free):
        self.name = name
        self.price = price
        self.category = category
        self.is_vege = is_vege
        self.gluten_free = gluten_free

class Drink(Menu):

    def __init__(self, name, price, category, volume, alc_percent):
        super().__init__(name, price, category, is_vege, gluten_free)
        self.volume = volume
        self.alc_percent = alc_percent

class Food(Menu):

    def __init__(self, name, price, description, category, serveSize):
        super().__init__(name, price, category, is_vege, gluten_free)
        self.serve_size = serveSize

