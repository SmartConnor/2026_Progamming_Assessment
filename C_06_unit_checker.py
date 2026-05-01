# Function
def unit_checker(question):
    """Makes sure that the user enters "yes / y" or "no / n" """

    while True:
        unit = input(question).lower()

        if unit == "g" or unit == "kg" or unit == "l" or unit == "ml":
            return "yes"
        elif unit == "gram" or unit == "grams" or unit == "kilogram" or unit == "kilograms":
            return "yes"
        elif unit == "Liter" or unit == "milliliters" or unit == "milliliter" or unit == "liter":
            return "yes"
        else:
            print("Please enter a valid unit (kg, g, ml or l)")

unit = unit_checker("Unit: ")