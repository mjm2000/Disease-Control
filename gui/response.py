import pygame
import pygame_gui

decreasearrowImg = pygame.image.load('art\\downvote.png')
increasingarrowImg = pygame.image.load('art\\upvote.png')
neutralcircleImg = pygame.image.load('art\\neutral.png')

#Creates down arrow
def downarrow(x, y):
    ourDisplay.blit(decreasearrowImg, (x + 20, y))

#Creates up arrow
def uparrow(x, y):
    ourDisplay.blit(increasingarrowImg, (x + 20, y))

def neutral(x, y):
    ourDisplay.blit(neutralcircleImg, (x + 20, y))






def yes_response(question_number, manager, texts):

    #clears out the previous week variable
    textsurface = myfont.render(str(results.week), False, (0, 0, 0))
    ourDisplay.blit(textsurface, (730, 70))

    #clears out the previous population variable
    textsurface = myfont.render(str(results.population) + "%", False, (0, 0, 0))
    ourDisplay.blit(textsurface, (700, 210))
    prevpopulation = int(results.population)

    #clears out the previous diseased variable
    textsurface = myfont.render(str(results.diseased) + "%", False, (0, 0, 0))
    ourDisplay.blit(textsurface, (700, 330))
    prevdiseased = int(results.diseased)

    #clears out the previous morale variable
    textsurface = myfont.render(str(results.morale) + "%", False, (0, 0, 0))
    ourDisplay.blit(textsurface, (700, 450))
    prevmorale = int(results.morale)

    #get proper results
    event_json = html_reader.json_reader()
    result = event_json['events'][question_number]['yes']
    mor = int(result[1])
    pop = int(result[2])
    dis = int(result[3])

    results.get_results(mor,pop,dis)

    # checks if the current pop percent is over the previous pop percent then
    # gives it an up arrow
    if(prevpopulation + pop) > prevpopulation:
        uparrow(740, 215)
    # checks if the current pop percent is under the previous pop percent then
    # gives it an down arrow
    elif(prevpopulation + pop) < prevpopulation:
        downarrow(740, 215)
    # nothing should happen since the percent didnt change
    else:
        neutral(740, 215)
        # print("no change p")

    # checks if the current morale percent is over the previous morale percent then
    # gives it an up arrow
    if(mor + prevmorale) > prevmorale:
        uparrow(740, 455)
    # checks if the current morale percent is under the previous morale percent then
    # gives it an down arrow
    elif(mor + prevmorale) < prevmorale:
        downarrow(740, 455)
    # nothing should happen since the percent didnt change
    else:
        neutral(740, 455)
        # print("no change m")

    # checks if the current diseased percent is over the previous diseased percent then
    # gives it an up arrow
    if(dis + prevdiseased) > prevdiseased:
        uparrow(740, 335)
    # checks if the current diseased percent is under the previous diseased percent then
    # gives it an down arrow
    elif(dis + prevdiseased) < prevdiseased:
        downarrow(740, 335)
    # nothing should happen since the percent didnt change
    else:
        neutral(740, 335)
        # print("no change d")


    #move to the next text box. We might want to change this later
    question_number = str(results.change_question(True))
    print(question_number)
    event_text_1 = pygame_gui.elements.ui_text_box.UITextBox(
        texts[question_number],
        relative_rect=pygame.Rect(
            (1,249),
            (598,150)
        ),
        manager=manager
    )



def no_response(question_number, manager, texts):

    #clears out the previous week variable
    textsurface = myfont.render(str(results.week), False, (0, 0, 0))
    ourDisplay.blit(textsurface, (730, 70))

    #clears out the previous population variable
    textsurface = myfont.render(str(results.population) + "%", False, (0, 0, 0))
    ourDisplay.blit(textsurface, (700, 210))
    prevpopulation = int(results.population)

    #clears out the previous diseased variable
    textsurface = myfont.render(str(results.diseased) + "%", False, (0, 0, 0))
    ourDisplay.blit(textsurface, (700, 330))
    prevdiseased = int(results.diseased)

    #clears out the previous morale variable
    textsurface = myfont.render(str(results.morale) + "%", False, (0, 0, 0))
    ourDisplay.blit(textsurface, (700, 450))
    prevmorale = int(results.morale)

    #get proper results
    event_json = html_reader.json_reader()
    result = event_json['events'][question_number]['no']
    mor = int(result[1])
    pop = int(result[2])
    dis = int(result[3])

    results.get_results(mor,pop,dis)

    # checks if the current pop percent is over the previous pop percent then
    # gives it an up arrow
    if(prevpopulation + pop) > prevpopulation:
        uparrow(740, 215)
    # checks if the current pop percent is under the previous pop percent then
    # gives it an down arrow
    elif(prevpopulation + pop) < prevpopulation:
        downarrow(740, 215)
    # nothing should happen since the percent didnt change
    else:
        neutral(740, 215)
        # print("no change p")

    # checks if the current morale percent is over the previous morale percent then
    # gives it an up arrow
    if(mor + prevmorale) > prevmorale:
        uparrow(740, 455)
    # checks if the current morale percent is under the previous morale percent then
    # gives it an down arrow
    elif(mor + prevmorale) < prevmorale:
        downarrow(740, 455)
    # nothing should happen since the percent didnt change
    else:
        neutral(740, 455)
        # print("no change m")

    # checks if the current diseased percent is over the previous diseased percent then
    # gives it an up arrow
    if(dis + prevdiseased) > prevdiseased:
        uparrow(740, 335)
    # checks if the current diseased percent is under the previous diseased percent then
    # gives it an down arrow
    elif(dis + prevdiseased) < prevdiseased:
        downarrow(740, 335)
    # nothing should happen since the percent didnt change
    else:
        neutral(740, 335)
        # print("no change d")

    #move to the next text box. We might want to change this later
    question_number = str(results.change_question(False))

    event_text_1 = pygame_gui.elements.ui_text_box.UITextBox(
        texts[question_number],
        relative_rect=pygame.Rect(
            (1,249),
            (598,150)
        ),
        manager=manager
    )

from event_test import results, html_reader
from gui.sideBar import myfont, ourDisplay