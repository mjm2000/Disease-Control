import random

week = 1
morale = 60
population = 100
diseased = 5

question = 1.1

low_chance = [0, 0, 0, 0, 1, 1, 1, 1, 2]
mid_chance = [0, 0, 1, 1, 1, 1, 1, 2, 2]
high_chance = [0, 0, 1, 1, 1, 2, 2, 2, 2]

def rand_choice():
    global morale
    rand_index = round(random.random() * 9) - 1
    if morale < 30:
        return low_chance[rand_index]
    elif 30 <= morale < 60:
        return mid_chance[rand_index]
    else:
        return high_chance[rand_index]


def change_question(yes_answer):
    global question

    if question < 4:
        if question == 1.1:
            question = 2.1
        elif question == 2.1:
            if yes_answer:
                question = 3.1
            else:
                question = 3.2
        elif 3 <= question < 4:
            if question == 3.1:
                if yes_answer:
                    question = 4.1
                else:
                    question = 4.0
            if question == 3.2:
                if yes_answer:
                    question = 4.2
                else:
                    question = 4.1
            question

    else:
        # make random number
        rand = rand_choice()
        rand /= 10
        question = round(question) + rand + 1

    return question


#randomly affects population decline
def randomizer(infected):
        if infected < 30:
            rand = random.randrange(0, 3, 1)
            rand = (rand / 10) * infected
            return round(rand)
        elif 30 <= infected < 60:
            rand = random.randrange(0, 6, 1)
            rand = (rand / 10) * infected
            return round(rand)
        else:
            rand = random.randrange(0, 10, 1)
            rand = (rand / 10) * infected
            return round(rand)

def get_results(mor, pop, dis):
    global week
    week += 1

    global morale
    morale += mor

    #need to subtract since this will most likely be a negative number
    global population
    global diseased
    population += pop - randomizer(diseased)
    if population < 0:
        population = 0

    diseased += dis + randomizer(diseased)
    if diseased > 100:
        diseased = 100


print(rand_choice())
