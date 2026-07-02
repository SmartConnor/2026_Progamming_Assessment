import pandas

# Function goes here
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
you can choose the unit of it (mL, L, g, kg) or press enter if it is an ingredient that doesn't need units.

After getting details about the recipe you will then need to give the details of
the ingredients that you have bought. 

This calculator will then calculate how much you actually need to make the dish according to the
difference between the recipe details and your bought ingredients.''')


def not_blank(question):
    """Checks that the users doesn't have a blank answer"""
    while True:

        response = input(question)

        # Checking if users put blank
        if response != "":
            return response

        print("Sorry, this cannot be blank. Please try again")


def unit_checker(question):
    """Checks that the users input valid answers"""

    while True:

        unit = input(question).lower()

        # returning the unit as the unit instead of yes
        if unit in ["kg", "kgs", "kilograms"]:
            return "kg"

        elif unit in ["g", "grams"]:
            return "g"

        elif unit in ["ml", "mls", "milliliters"]:
            return "ml"

        elif unit in ["l", "liters"]:
            return "l"

        elif unit == "":
            return "-"

        else:
            print("Please enter a valid unit. (kg, g, ml or l)")


def ingredient_checker(question):
    """Checks that the users doesn't have a blank answer or a number answer"""
    while True:

        response = input(question)

        # Checking that it can't be blank
        if response == "":
            print("Sorry, this cannot be blank. Please try again")
            continue

        # Checking that users don't put numbers
        for item in response:
            if item.isdigit():
                print("Sorry, this cannot have a number. Please try again")
                break

        else:
            return response


# Tittle of the calculator
print(make_statement("Welcome to Recipe Calculator", "📃"))
print()

# Asking users if they want instruction
want_instructions = yes_no_checker("Do you want to see the instruction? ")
print()

if want_instructions == "yes":
    instruction()
print()

# Main routine

# Getting Recipe name
recipe_name = not_blank("Recipe Name: ")
print()

# Getting the serving size
serving_size = num_check("serving size: ")
print()

# List for recipe details
all_ing = []
all_amount = []
all_bought_unit = []
all_recipe = []
all_recipe_unit = []
all_price = []
all_cost = []

looping = ""
# This is where looping starts
while looping != "no":

    if looping == "no":
        break

    print()
    # Asking for ingredient name
    ing = ingredient_checker("Ingredient: ")
    print()

    # Getting the amount the recipe needs
    recipe_amount = num_check("Recipe Amount: ")
    print()

    # Getting the recipe unit
    recipe_unit = unit_checker("Recipe Unit <enter> for no unit: ")
    print()

    # Getting the amount bought
    bought_amount = num_check("Bought Amount: ")
    print()

    # Getting the unit bought
    bought_unit = unit_checker("Bought Unit <enter> for no unit: ")
    print()

    # Getting the price
    price = num_check("Price($): ")
    print()

    # Naming it different to put in panda dataframe
    bought_details = bought_amount
    recipe_details = recipe_amount

    # Making the grams and milliliters the default
    # Converting the units to a default
    if recipe_unit == "kg":
        recipe_amount = recipe_amount * 1000

    if recipe_unit == "l":
        recipe_amount = recipe_amount * 1000

    if bought_unit == "kg":
        bought_amount = bought_amount * 1000

    if bought_unit == "l":
        bought_amount = bought_amount * 1000

    # Calculating the Cost to make
    Cost_to_make = price / bought_amount * recipe_amount
    print(f"Cost To Make: ${Cost_to_make:.2f} ")


    # Appending the recipe details but make it append
    # "-" if the ingredient doesn't need unit
    if ing == "":
        # list to hold recipe details
        all_ing.append(ing)
        all_amount.append(bought_details)
        all_recipe.append(recipe_details)
        all_price.append(price)
        all_cost.append(Cost_to_make)
        all_bought_unit.append("-")
        all_recipe_unit.append("-")

    else:
        # list to hold recipe details
        all_ing.append(ing)
        all_amount.append(bought_details)
        all_bought_unit.append(bought_unit)
        all_recipe.append(recipe_details)
        all_recipe_unit.append(recipe_unit)
        all_price.append(price)
        all_cost.append(Cost_to_make)

    looping = yes_no_checker("Do you want to continue? ")
    print()

# Recipe headings
recipe_heading = {
    'Ing': all_ing,
    'Bought(A)': all_amount,
    'Bought(U)': all_bought_unit,
    'Recipe(A)': all_recipe,
    'Recipe(U)': all_recipe_unit,
    'Price($)': all_price,
    'Cost to make($)': all_cost,
}

# Creating dataframe
recipe_data = pandas.DataFrame(recipe_heading)
# Calculating the Total cost
total_cost = recipe_data['Cost to make($)'].sum()
# Calculating per serve
per_serve = total_cost / serving_size

# printing the data frame
print(make_statement("Recipe Data", "📊"))
print(recipe_data)
print()
print("Total Cost")
print(f"${total_cost:.2f}")
print()
print("Per Serve")
print(f"${per_serve:.2f}")


