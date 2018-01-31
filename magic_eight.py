def user_question():
    user_input = input("What is your quesiton? ")
    return user_input

import random
possible_answers = ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely",
                    "You may rely on it", "As I see it, yes", "Most likely", "Outlook good","Yes", "Signs point to yes", "Ask again later", "Better not to tell you now", "Cannot predict now",
                    "Concentrate and ask again", "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good",
                    "Very doubtful"]

answer_to_question = random.choice(possible_answers)
