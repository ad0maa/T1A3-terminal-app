entrees = {
    'Karaage Chicken': 8,
    'Edamame': 6,
    'Beef Tataki': 10,
    'Pork Gyoza': 7,
    'Vegetarian Gyoza': 7,
    'Agedashi Todu': 8.5,
}


ramen = {
    'Tonkatsu Ramen': 17,
    'Spicy Pork Ramen': 18,
    'Chicken Ramen': 18,
    'Miso Ramen': 18,
    'Vegetarian Ramen':17
}

main = {
    'Chicken Katsu Don': 18,
    'Beef Curry': 17,
    'Teriyaki Chicken': 15,
    'Mixed Bento Box': 18.5,
}

sushi = {
    'Cooked Tuna Roll': 5,
    'California Roll': 5,
    'Vegetarian Roll': 4,
    'Prawn Roll': 5,
    'Salmon Sashimi': 10,
}

drinks = {
    'Coca-Cola': 3,
    'Coca-Cola Zero': 3,
    'Sprite': 3,
    'Gingerbeer': 4,
    'Iced Tea': 4,
}



def print_menu(name):
    for k,v in name.items():
        print (k + ' $' + str(v))

# print_menu(entree_menu)