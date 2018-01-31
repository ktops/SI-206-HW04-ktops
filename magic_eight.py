def user_question():
    user_input = input("What is your quesiton? ")
    return user_input

user_input = ""
while user_input is not "quit":
    user_input = user_question()

    if user_input[-1] is not "?":
        print("I'm sorry, I can only answer questions.")
    else:
        break
