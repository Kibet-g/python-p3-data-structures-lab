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
    # Return a list of the names of each spicy food
    return [food['name'] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    # Return a list of foods with heat_level > 5
    return [food for food in spicy_foods if food['heat_level'] > 5]

def print_spicy_foods(spicy_foods):
    # Print each spicy food formatted with chili pepper emojis based on heat level
    for food in spicy_foods:
        heat_emoji = "🌶" * food['heat_level']
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_emoji}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    # Return a dictionary representing the spicy food that matches the cuisine
    for food in spicy_foods:
        if food['cuisine'] == cuisine:
            return food
    return None

def print_spiciest_foods(spicy_foods):
    # Print only the spiciest foods (heat_level > 5) formatted with chili pepper emojis
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)

def get_average_heat_level(spicy_foods):
    # Return the average heat level of the spicy foods
    total_heat = sum(food['heat_level'] for food in spicy_foods)
    return total_heat // len(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    # Add a new spicy food to the list and return the updated list
    spicy_foods.append(spicy_food)
    return spicy_foods
