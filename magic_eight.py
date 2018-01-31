def user_question():
    user_input = input("What is your quesiton? ")
    return user_input

import random
questions_list=  ["Ask again later", "Better not to tell you now", "Cannot predict now",
                "Concentrate and ask again", "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good",
                "Very doubtful"]
answer_to_question = random.choice(questions_list)
