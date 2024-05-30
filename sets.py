from sets_categories_data import (ALCOHOLS)

def clean_ingredients(dish_name, dish_ingredients):
    dish_ingredients_set = set(dish_ingredients)
    final_dish = dish_name, dish_ingredients_set 
    return final_dish

from sets_categories_data import ALCOHOLS 
def check_drinks(drink_name, drink_ingredients):
    for alcohol in drink_ingredients:
        if alcohol in ALCOHOLS: 
            return f"{drink_name} Cocktail"
    return f"{drink_name} Mocktail"
