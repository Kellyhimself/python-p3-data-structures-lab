# Define a list of dictionaries representing different types of spicy foods
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

# Function to get a list of names of all spicy foods in the provided list
def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]

# Function to get a list of spiciest foods with heat level greater than 5
def get_spiciest_foods(spicy_foods):
    spiciest_foods = [food for food in spicy_foods if food["heat_level"] > 5]
    return spiciest_foods

# Function to print the details of all spicy foods
def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat_level = "🌶" * food["heat_level"]  # Assign emoji based on the heat level
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level}")  # Print food name, cuisine, and heat level

# Function to get the first spicy food that matches a specific cuisine
def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    match = [food for food in spicy_foods if food["cuisine"] == cuisine]
    return match[0] if match else None  # Return the first match or None if no match found

# Function to print details of the spiciest foods
def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)  # Get the list of spiciest foods
    for food in spiciest_foods:
        heat_level = "🌶" * food["heat_level"]  # Assign emoji based on the heat level
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level}")  # Print spiciest food details

# Function to calculate the average heat level of all spicy foods
def get_average_heat_level(spicy_foods):
    listf = [food["heat_level"] for food in spicy_foods]  # Extract heat levels into a list
    return sum(listf)/len(listf)  # Calculate and return the average heat level

# Function to add a new spicy food to the list of spicy foods
def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)  # Add the new spicy food to the list
    return spicy_foods  # Return the updated list of spicy foods