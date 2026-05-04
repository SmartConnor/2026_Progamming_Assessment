def not_blank(question):
    """Checks that the users doesn't have a blank answer"""
    while True:

        response = input(question)

        if response != "":
            return response

        print("Sorry, this cannot be blank. Please try again")


txt = not_blank("Enter an ingredient: ")

for item in txt:
    if item.isdigit():
        print("we have a number")
                