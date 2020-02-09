
import pygame
import pygame_gui
import gui.sideBar
from pygame.locals import *
from event_test import results

from event_test import html_reader

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

answers = {
    "1.1":
        {
            "pop": (0, -5),
            "mor": (0, -7),
            "dis": (0, 5)
        },
    "2.1":
        {
            "pop": (0, -6),
            "mor": (7, -7),
            "dis": (0, 6),
        },
    "3.1":
        {
            "pop": (0, -8),
            "mor": (7, 5),
            "dis": (0, 8)
        },
    "4.1":
        {
            "pop": (0, -5),
            "mor": (7, -1),
            "dis": (0, 5)
        },
    "5.1":
        {
            "pop": (0, -9),
            "mor": (7, 0),
            "dis": (0, 9)
        },
    "6.1":
        {
            "pop": (0, -5),
            "mor": (7, -7),
            "dis": (0, 5)
        }
}

mayor = ""
city = ""

#questions = html_reader(mayor, city)


text_index = 0
global ourDisplay, display_width,display_height,clock

def run_game():
    pygame.init()
    pygame.display.set_caption('Disease Control')

    white = (255,255,255)
    red = (255,0,0)
    black = (0,0,0)


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

    is_running = True
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False


            #CLicking the buttons
            if event.type == MOUSEBUTTONDOWN:
                mouse_pos = event.pos # Now it will have the coordinates of click point.
                if yesButtonPosition.collidepoint(mouse_pos):
                    textsurface = myfont.render(str(results.week), False, (0, 0, 0))
                    ourDisplay.blit(textsurface, (730, 70))

                    #clears out the previous population variable
                    textsurface = myfont.render(str(results.population) + "%", False, (0, 0, 0))
                    ourDisplay.blit(textsurface, (700, 210))

                    #clears out the previous diseased variable
                    textsurface = myfont.render(str(results.diseased) + "%", False, (0, 0, 0))
                    ourDisplay.blit(textsurface, (700, 330))

                    #clears out the previous morale variable
                    textsurface = myfont.render(str(results.morale) + "%", False, (0, 0, 0))
                    ourDisplay.blit(textsurface, (700, 450))

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
                    textsurface = myfont.render(str(results.week), False, (0, 0, 0))
                    ourDisplay.blit(textsurface, (730, 70))

                    #clears out the previous population variable
                    textsurface = myfont.render(str(results.population) + "%", False, (0, 0, 0))
                    ourDisplay.blit(textsurface, (700, 210))

                    #clears out the previous diseased variable
                    textsurface = myfont.render(str(results.diseased) + "%", False, (0, 0, 0))
                    ourDisplay.blit(textsurface, (700, 330))

                    #clears out the previous morale variable
                    textsurface = myfont.render(str(results.morale) + "%", False, (0, 0, 0))
                    ourDisplay.blit(textsurface, (700, 450))
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
def text_objects(text, font):
    black = (0,0,0)
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
def game_intro():

    intro = True
    clock = pygame.time.Clock()
    display_width = 800
    display_height = 600
    ourDisplay = pygame.display.set_mode((display_width,display_height))
    myfont = pygame.font.SysFont('Comic Sans MS', 40)
    white =(255,255,255)
    exitImg = pygame.image.load('exitButton.png')
    playImg = pygame.image.load('startButton.png')

    playImgPosition = Rect(100,0,0,400)
    playImgPosition.collidepoint(pygame.mouse.get_pos())
    playImgPosition = playImg.get_rect()
    playImgPosition = playImgPosition.move(275,350)

    exitImgPosition = Rect(200,0,0,500)
    exitImgPosition.collidepoint(pygame.mouse.get_pos())
    exitImgPosition = exitImg.get_rect()
    exitImgPosition = exitImgPosition.move(275,450)


    background = pygame.image.load('titleScreen.png')

    while intro:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                mouse_pos = event.pos # Now it will have the coordinates of click point.
                if playImgPosition.collidepoint(mouse_pos):
                    intro = False
                if exitImgPosition.collidepoint(mouse_pos):
                    exit()

        ourDisplay.blit(background,(0,0))
        #TextSurf, TextRect = text_objects('Disease Control', largeText)
        textsurface = myfont.render('Disease Control', False,white)
        #text_rect = TextRect.get_rect(center=(display_width/2, display_height))

        ourDisplay.blit(textsurface,(250,0))
        ourDisplay.blit(playImg, playImgPosition)
        ourDisplay.blit(exitImg, exitImgPosition)
        pygame.display.update()
        clock.tick(15)



game_intro()
run_game()

















