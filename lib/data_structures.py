def get_names(spicy_foods):
    """Returns a list of names of each spicy food."""
    return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    """Returns a list of foods with heat level > 5."""
    return [food for food in spicy_foods if food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    """Prints each spicy food in the specified format."""
    for food in spicy_foods:
        heat_emojis = "🌶" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_emojis}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    """Returns the food dictionary matching the given cuisine."""
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None

def print_spiciest_foods(spicy_foods):
    """Prints only the spiciest foods (heat level > 5)."""
    spiciest = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest)

def get_average_heat_level(spicy_foods):
    """Returns the average heat level of all spicy foods."""
    total = sum(food["heat_level"] for food in spicy_foods)
    return total // len(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    """Adds a new spicy food to the list and returns the updated list."""
    return spicy_foods + [spicy_food]