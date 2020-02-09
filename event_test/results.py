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
        rand = rand_choice()
        rand /= 10
        question = round(question) + rand + 1


#randomly affects population decline
def randomizer(infected):
        if infected < 30:
            rand = random.randrange(0, 0.3, 0.05)
            rand = rand * infected
            return round(rand)
        elif 30 <= infected < 60:
            rand = random.randrange(0, 0.6, 0.05)
            rand = rand * infected
            return round(rand)
        else:
            rand = random.randrange(0, 1.0, 0.05)
            rand = rand * infected
            return round(rand)

def get_results(pop, mor, dis):
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
