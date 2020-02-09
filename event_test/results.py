week = 1
morale = 60
population = 100
diseased = 5

tier = 1

def get_results(pop, mor, dis):
    global week
    week += 1

    global morale
    morale += mor

    global population
    population += pop

    global diseased
    diseased += dis

    #update tiers if necessary
    if morale > 80:
        tier = 2

    elif morale < 40:
        tier = 0

    else:
        tier = 1