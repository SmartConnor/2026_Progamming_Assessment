# Function goes here
def unit_checker(question):
    """Checks that the users input valid answers"""

    while True:

        unit = input(question).lower()

        # returning the unit
        if unit in ["kg", "kgs", "kilograms"]:
            return "kg"

        elif unit in ["g", "grams"]:
            return "g"

        elif unit in ["ml", "mls", "milliliters"]:
            return "ml"

        elif unit in ["l", "liters"]:
            return "l"

        else:
            print("Please enter a valid unit. (kg, g, ml or l)")

