from unicodedata import category


class Menu:
    
    def __init__(self, name, price, category, is_vege, gluten_free):
        self.name = name
        self.price = price
        self.category = category
        self.is_vege = is_vege
        self.gluten_free = gluten_free

    # STEVES FIRST VERSION
    def print_entree(self):
        if self.category == "Entree":
            print(f'Item: {self.name} ${self.price}!!')

    def print_main(self):
        if self.category == "Ramen":
            print(f'Item: {self.name} ${self.price}!!')


    def gluten_list(self):
        if self.gluten_free == True:
            print(f'Item: {self.name} is a gluten free option')

    # def print_menu(self):
    #     print(f'Item: {self.name} $ {self.price}!!')
    #     self.category('Entree')

    def __str__(self, category='Entree'):
        return "The {name} food {price} healthy.".format(name=self.name, healthyStatus=self.name)


class Drink(Menu):

    def __init__(self, name, price, category, volume, alc_percent):
        super().__init__(name, price, category, is_vege, gluten_free)
        self.volume = volume
        self.alc_percent = alc_percent

class Food(Menu):

    def __init__(self, name, price, description, category, serveSize):
        super().__init__(name, price, category, is_vege, gluten_free)
        self.serve_size = serveSize




karaage = Menu('Karaage Chicken', 8,'Entree', False,  False)
edamame = Menu('Edamame', 6, 'Entree', True, True)
beef_tataki = Menu('Beef Tataki', 10, 'Entree', False, True)
pork_gyoza = Menu('Pork Gyoza', 7, 'Entree', False, False)
veggie_gyoza = Menu('Vegetarian Gyoza', 7, 'Entree', True, False)
age_tofu = Menu('Agedashi Todu', 8.5, 'Entree', True, True)


tonk_ramen = Menu('Tonkatsu Ramen', 17, 'Ramen', False, False)
spicy_ramen = Menu('Spicy Pork Ramen', 18, 'Ramen', False, False)
chick_ramen = Menu('Chicken Ramen', 18, 'Ramen', False, False)
miso_ramen = Menu('Miso Ramen', 18, 'Ramen', False, False)
veggie_ramen = Menu('Vegetarian Ramen', 17, 'Ramen', True, False)


items = [karaage, edamame, beef_tataki, miso_ramen, veggie_ramen]


# for food in items:
#     food.print_menu()

print("Entree")
for food in items:
    food.print_entree()

print("Mains")
for food in items:
    food.print_main()

print("Gluten")
for food in items:
    food.gluten_list()