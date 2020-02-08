global week
week = 1

global morale
morale = 100

global population
population = 100

global diseased
diseased = 5

def get_results(mor, pop, dis):
    week += 1
    morale += mor
    population += pop
    diseased += dis