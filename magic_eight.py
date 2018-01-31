def user_question():
    user_input = input("What is your quesiton? ")
    return user_input

possible_answers = ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely",
                    "You may rely on it", "As I see it, yes", "Most likely", "Outlook good","Yes", "Signs point to yes"]

answer_to_question = random.choice(possible_answers)
