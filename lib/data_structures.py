import ipdb

spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    each_food = [food.get("name") for food in spicy_foods]
    return each_food
    # each_food = []
    # for food in spicy_foods:
        # each_food.append(food.get("name"))
    # return each_food
    pass

def get_spiciest_foods(spicy_foods):
   spiciest_foods = [food for food in spicy_foods if food.get("heat_level") > 5]
   return spiciest_foods

    # spiciest_foods = []
    # for food in spicy_foods:
    #     if food.get('heat_level', 0) > 5:
    #         spiciest_foods.append(food)
    #     return spiciest_foods
    # pass

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
            food_name = food.get("name")
            food_cuisine = food.get("cuisine")
            food_heat = "🌶" * food.get("heat_level")
            print(f'{food_name} ({food_cuisine}) | Heat Level: {food_heat}')
            pass
    


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food.get("cuisine") == cuisine:
            return food

def print_spiciest_foods(spicy_foods):
        for food in spicy_foods:
            if food.get("heat_level") > 5:
                food_name = food.get("name")
                food_cuisine = food.get("cuisine")
                food_heat = "🌶" * food.get("heat_level")
                print(f'{food_name} ({food_cuisine}) | Heat Level: {food_heat}')
            pass

def get_average_heat_level(spicy_foods):
    heat_list = [food.get("heat_level") for food in spicy_foods]
    heat_average = sum(heat_list)/len(heat_list)
    return heat_average
    pass

def create_spicy_food(spicy_foods, spicy_food):
    return spicy_foods + [spicy_food]
