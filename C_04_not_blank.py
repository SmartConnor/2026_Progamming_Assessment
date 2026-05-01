# Function goes here
def not_blank(question):
    """Checks that the users doesn't have a blank answer"""
    while True:

        response = input(question)

        if response != "":
            return response

        print("Sorry, this cannot be blank. Please try again")
