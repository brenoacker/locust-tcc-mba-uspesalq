import random
import string
import uuid

from utils.common.create_user import generate_random_string


def generate_unique_burger_name():
    name = generate_random_burger_name()
    name = f"{name} {generate_random_string(8)}"
    return name

def generate_random_burger_name(length=8):
    adjectives = ["Juicy", "Spicy", "Crispy", "Cheesy", "Grilled"]
    nouns = ["Burger", "Delight", "Feast", "Treat", "Bite"]
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    random_string = uuid.uuid4()
    return f"{adjective} {noun} {random_string}"

def generate_unique_drink_name():
    name = generate_random_drink_name()
    name = f"{name} {generate_random_string(8)}"
    return name

def generate_random_drink_name(length=8):
    adjectives = ["Refreshing", "Cool", "Sparkling", "Fizzy", "Chilled"]
    nouns = ["Soda", "Juice", "Smoothie", "Cocktail", "Shake"]
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    random_string = uuid.uuid4()
    return f"{adjective} {noun} {random_string}"

def generate_unique_dessert_name():
    name = generate_random_dessert_name()
    name = f"{name} {generate_random_string(8)}"
    return name

def generate_random_dessert_name(length=8):
    adjectives = ["Sweet", "Delicious", "Creamy", "Fruity", "Chocolaty"]
    nouns = ["Cake", "Pie", "Pudding", "Tart", "Brownie"]
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    random_string = uuid.uuid4()
    return f"{adjective} {noun} {random_string}"

def generate_unique_side_dish_name():
    name = generate_random_side_dish_name()
    name = f"{name} {generate_random_string(8)}"
    return name

def generate_random_side_dish_name(length=8):
    adjectives = ["Crispy", "Savory", "Spicy", "Cheesy", "Garlic"]
    nouns = ["Fries", "Salad", "Wedges", "Rings", "Sticks"]
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    random_string = uuid.uuid4()
    return f"{adjective} {noun} {random_string}"