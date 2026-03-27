# Function goes here
def make_statement(statement, decoration):
    """Makes the heading stand out with decorations"""

    print(f"{decoration} {statement} {decoration}")


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
This is the Instructions
Please follow the instructions.''')


print(make_statement("Recipe", "📃"))
print()

want_instructions = yes_no_checker("Do you want to see the instruction?")
print()

if want_instructions == "yes":
    instruction()
