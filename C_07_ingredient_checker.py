def ingredient_checker(question):
    """Checks that the users doesn't have a blank answer"""
    while True:

        response = input(question)

        if response == "":
            print("Sorry, this cannot be blank. Please try again")
            continue

        for item in response:
            if item.isdigit():
                print("Sorry, this cannot have a number. Please try again")
                break

        else:
            return response