# Function goes here
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


# Main routine
while True:
    want_instruction = yes_no_checker("Do you want to see instruction? ")
    print(f"You picked {want_instruction}")
