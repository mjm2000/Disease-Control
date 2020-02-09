
import pygame
import pygame_gui
import gui.sideBar
from pygame.locals import *
from event_test import results

#this is just some dummy data
texts = [
    {
        "text": "<p>A man has fallen into the river in lego city!</p>",
        "pop_y": "0",
        "mor_y": "7",
        "dis_y": "0",
        "pop_n": "-5",
        "mor_n": "-7",
        "dis_n": "0"
    },
    {
        "text": "<p>Start the new rescue helicopter!</p>",
        "pop_y": "0",
        "mor_y": "7",
        "dis_y": "0",
        "pop_n": "-5",
        "mor_n": "-7",
        "dis_n": "5"
    },
    {
        "text": "<p>HEY!!</p>",
        "pop_y": "0",
        "mor_y": "7",
        "dis_y": "0",
        "pop_n": "-5",
        "mor_n": "-7",
        "dis_n": "5"
    },
    {
        "text": "<p>Build the helicopter and off to the rescue!</p>",
        "pop_y": "0",
         "mor_y": "7",
        "dis_y": "0",
        "pop_n": "-5",
        "mor_n": "-7",
        "dis_n": "5"
    },
    {
        "text": "<p>Prepare the lifeline!</p>",
        "pop_y": "0",
        "mor_y": "7",
        "dis_y": "0",
        "pop_n": "-5",
        "mor_n": "-7",
        "dis_n": "5"
    },
    {
        "text": "<p>Lower the stretcher!</p>",
        "pop_y": "0",
        "mor_y": "7",
        "dis_y": "0",
        "pop_n": "-5",
        "mor_n": "-7",
        "dis_n": "5"
    },
    {
        "text": "<p>And make the rescue!</p>",
        "pop_y": "0",
        "mor_y": "7",
        "dis_y": "0",
        "pop_n": "-5",
        "mor_n": "-7",
        "dis_n": "5"
    }
]

text_index = 0
def run_game():
    pygame.init()
    pygame.display.set_caption('Disease Control')

    white = (255,255,255)
    red = (255,0,0)

    display_width = 800
    display_height = 600
    ourDisplay = pygame.display.set_mode((display_width,display_height))

    manager = pygame_gui.UIManager((800, 600))

    #Load Images
    noButtonImg = pygame.image.load('redButton.png')
    noButtonImgHover = pygame.image.load('redButtonHover.png')

    yesButtonImg = pygame.image.load('greenButtonwoop.png')
    yesButtonHover = pygame.image.load('greenButton.png')
    backgroundImage = pygame.image.load('background.png')

    decreasearrowImg = pygame.image.load('downvote.png')
    increasingarrowImg = pygame.image.load('upvote.png')\

    personImg = pygame.image.load('person.png')


    #This is the yes Button
    yesButtonPosition = Rect(0,0,0,400)
    yesButtonPosition.collidepoint(pygame.mouse.get_pos())
    yesButtonPosition = yesButtonImg.get_rect()
    yesButtonPosition = yesButtonPosition.move(0,400)

    #This is the No button
    noButtonPosition = Rect(0,300,0,400)
    noButtonPosition.collidepoint(pygame.mouse.get_pos())
    noButtonPosition = noButtonImg.get_rect()
    noButtonPosition = noButtonPosition.move(300,400)

    #Creates down arrow
    def downarrow(x, y):
        ourDisplay.blit(decreasearrowImg, (x + 20, y))

    #Creates up arrow
    def uparrow(x, y):
        ourDisplay.blit(increasingarrowImg, (x + 80, y))

    #these are the texts for the sidebar
    myfont = pygame.font.SysFont('Comic Sans MS', 20)


    #this is the text box

    #Creating the first instance of the text box
    global text_index
    event_text_1 = pygame_gui.elements.ui_text_box.UITextBox(
        texts[text_index]['text'],
        relative_rect=pygame.Rect(
            (1,249),
            (598,150)
        ),
        manager=manager
    )

    #Increments through the dummy data dictionary
    text_index = 0

    is_running = True
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False


            #CLicking the buttons
            if event.type == MOUSEBUTTONDOWN:
                mouse_pos = event.pos # Now it will have the coordinates of click point.
                if yesButtonPosition.collidepoint(mouse_pos):
                    textsurface = myfont.render("%", False, (255, 0, 0))

                    #get proper results
                    result = texts[text_index]
                    pop = int(result["pop_y"])
                    mor = int(result["mor_y"])
                    dis = int(result["dis_y"])

                    results.get_results(0, 5, 0)


                    #move to the next text box. We might want to change this later
                    text_index += 1

                    event_text_1 = pygame_gui.elements.ui_text_box.UITextBox(
                        texts[text_index]['text'],
                        relative_rect=pygame.Rect(
                            (1,249),
                            (598,150)
                        ),
                        manager=manager
                    )

                if noButtonPosition.collidepoint(mouse_pos):
                    #keeps track of current question

                    #Goes over the current percentage and coloring it red and creating the down arror
                    #for each category
                    textsurface = myfont.render("%", False, (255, 0, 0))
                    ourDisplay.blit(textsurface, (730, 200))
                    ourDisplay.blit(textsurface, (730, 320))
                    ourDisplay.blit(textsurface, (730, 440))
                    downarrow(730, 200)
                    downarrow(730, 320)
                    downarrow(730, 440)
                    #get proper results
                    result = texts[text_index]
                    pop = int(result["pop_n"])
                    mor = int(result["mor_n"])
                    dis = int(result["dis_n"])

                    results.get_results(-5, -6, -5)

                    #move to the next text box. We might want to change this later
                    text_index += 1

                    event_text_1 = pygame_gui.elements.ui_text_box.UITextBox(
                        texts[text_index]['text'],
                        relative_rect=pygame.Rect(
                            (1,249),
                            (598,150)
                        ),
                        manager=manager
                    )

            manager.process_events(event)
        #Hover on yes button
        if yesButtonPosition.collidepoint(pygame.mouse.get_pos()):
            ourDisplay.blit(yesButtonHover, yesButtonPosition)
        else:
            ourDisplay.blit(yesButtonImg,yesButtonPosition)

        #Hover on no button
        if noButtonPosition.collidepoint(pygame.mouse.get_pos()):
            ourDisplay.blit(noButtonImgHover, noButtonPosition)
        else:
            ourDisplay.blit(noButtonImg,noButtonPosition)




        ourDisplay.blit(backgroundImage,(0,0))
        ourDisplay.blit(personImg,(175,10))


        #pygame.draw.rect(ourDisplay,black,(600,0,700,600))
        gui.sideBar.weektitle(660,70)
        gui.sideBar.weekvariable(730, 70)

        # should be 30 away from its corresponding variable
        # the 3rd argument is the variable
        gui.sideBar.totalpoptitle(625, 180)
        gui.sideBar.totalpopvariable(700, 210)

        gui.sideBar.diseasedtitle(625, 300)
        gui.sideBar.diseasedvariable(700, 330)

        gui.sideBar.moraletitle(660, 420)
        gui.sideBar.moralevariable(700, 450)

        #draws the textbox
        manager.draw_ui(ourDisplay)

        pygame.display.update()

run_game()

















