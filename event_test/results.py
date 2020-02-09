import random
week = 1
morale = 60
population = 100
diseased = 5

question = 1.1

def change_question(yes_answer):
    global question

    if question < 4:
        if question == 1:
            question = 2
        elif question == 2:
            if yes_answer:
                question = 3.1
            else:
                question = 3.2
        elif 3 <= question < 4:
            if yes_answer:
                question += 1
            else:
                question += 0.9
    else:
        # make random number
        rand = random.randint(0,3)
        rand /= 10
        question = round(question) + rand + 1



def get_results(pop, mor, dis):
    global week
    week += 1

    global morale
    morale += mor

    global population
    population += pop

    global diseased
    diseased += dis

question = 2.2

change_question(True)

print(question)