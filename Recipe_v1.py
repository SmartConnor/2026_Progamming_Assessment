def make_statement(statement, decoration):
    """Makes the heading stand out with decorations"""

    return f"{decoration * 3} {statement} {decoration * 3}"


def num_check(question):
    error = "Please enter a number that is more than zero\n"
    while True:

        try:
            # ask the user for a number
            response = float(input(question))

            # check that the number is more than zero
            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


def yes_no_checker(question):
    """Makes sure that the user enters "yes / y" or "no / n" """

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes / y or no / n")


def instruction():
    make_statement("Instructions", "")

    print('''

This is the instruction    

This is a recipe calculator, you will first need to give the recipe name,
then you will give the ingredients and the amount of that ingredient. After getting the ingredients,
you can choose the unit of it (mL, L, g, kg).''')


def not_blank(question):
    """Checks that the users doesn't have a blank answer"""
    while True:

        response = input(question)

        if response != "":
            return response

        print("Sorry, this cannot be blank. Please try again")


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


print(make_statement("Welcome to Recipe Calculator", "📃"))
print()

want_instructions = yes_no_checker("Do you want to see the instruction?")
print()

if want_instructions == "yes":
    instruction()
print()

# Main routine

# Getting Recipe name, and ingredient
recipe_name = not_blank("Recipe Name: ")
print(f"Recipe Name is {recipe_name}")
print()

serving_size = num_check("serving size: ")
print(f"Serving Size is {serving_size}")
print()

ing = ""
# This is where looping starts
while ing != "xxx":

    print()
    # The ingredients
    ing = not_blank("Ingredient: ")
    print()

    # Breaking the loop
    if ing == "xxx":
        break

    # Making it skip the unit if the ingredient is eggs
    if ing == "egg" or ing == "eggs":

        # The amount of the ingredient
        amount = num_check("Amount: ")
        print()

    else:
        # The amount of the ingredient
        amount = num_check("Amount: ")
        print()

        # The unit of the amount (kg, g, l, ml)
        unit = unit_checker("Unit: ")








