week = 1
morale = 100
population = 100
diseased = 5

def get_results(pop, mor, dis):
    global week
    week += 1

    global morale
    morale += mor

    global population
    population += pop

    global diseased
    diseased += dis