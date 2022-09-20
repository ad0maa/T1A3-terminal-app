import menu

# Create menu items

#Entrees
karaage = menu.Menu('Karaage Chicken', 8,'Entree', False,  False)
edamame = menu.Menu('Edamame', 6, 'Entree', True, True)
beef_tataki = menu.Menu('Beef Tataki', 10, 'Entree', False, True)
pork_gyoza = menu.Menu('Pork Gyoza', 7, 'Entree', False, False)
veggie_gyoza = menu.Menu('Vegetarian Gyoza', 7, 'Entree', True, False)
age_tofu = menu.Menu('Agedashi Todu', 8.5, 'Entree', True, True)

# Ramen
tonk_ramen = menu.Menu('Tonkatsu Ramen', 17, 'Ramen', False, False)
spicy_ramen = menu.Menu('Spicy Pork Ramen', 18, 'Ramen', False, False)
chick_ramen = menu.Menu('Chicken Ramen', 18, 'Ramen', False, False)
miso_ramen = menu.Menu('Miso Ramen', 18, 'Ramen', False, False)
veggie_ramen = menu.Menu('Vegetarian Ramen', 17, 'Ramen', True, False)

# Mains
katsu_don = menu.Menu('Chicken Katsu Don', 18, 'Main', False, False)
beef_curry = menu.Menu('Beef Curry', 17, 'Main', False, True)
teri_chicken = menu.Menu('Teriyaki Chicken', 15, 'Main', False, True)
bento_box = menu.Menu('Mixed Bento Box', 18.5, 'Main', False, True)

# Sushi 

tuna_roll = menu.Menu('Cooked Tuna Roll', 5, 'Sushi', False, True)
cali_roll = menu.Menu('California Roll', 5, 'Sushi', False, True)
vege_roll = menu.Menu('Vegetarian Roll', 4, 'Sushi', True, True)
prawn_roll = menu.Menu('Prawn Roll', 5, 'Sushi', False, True)
salmon_sash = menu.Menu('Salmon Sashimi', 10, 'Sushi', False, True)

# Drinks
coke = menu.Menu('Coca-Cola', 3, 'Drinks', True, True)
coke_zero = menu.Menu('Coca-Cola Zero', 3, 'Drinks', True, True)
sprite = menu.Menu('Sprite', 3, 'Drinks', True, True)
ginger_beer = menu.Menu('Gingerbeer', 4, 'Drinks', True, True)
iced_tea = menu.Menu('Iced Tea', 4, 'Drinks', True, True)

