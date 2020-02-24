import pygame
import pygame_gui
import gui.sideBar
import gui.pygame_textinput
import gui.intro
import gui.playerInput
import gui.response

from pygame.locals import *
from event_test import results
from event_test import html_reader

#from event_test import html_reader
gui.intro.game_intro()

#questions = html_reader(mayor, city)
text_index = 0
global ourDisplay, display_width,display_height,clock

def run_game():
    pygame.init()
    pygame.display.set_caption('Disease Control')

    #These are the colors white red and black
    white = (255,255,255)
    red = (255,0,0)
    black = (0,0,0)

    display_width = 800
    display_height = 600
    ourDisplay = pygame.display.set_mode((display_width,display_height))
    manager = pygame_gui.UIManager((800, 600))

    #Load Images
    noButtonImg = pygame.image.load('art\\redButton.png')
    noButtonImgHover = pygame.image.load('art\\redButtonHover.png')

    yesButtonImg = pygame.image.load('art\\greenButtonwoop.png')
    yesButtonHover = pygame.image.load('art\\greenButton.png')
    backgroundImage = pygame.image.load('art\\background.png')

    personImg = pygame.image.load('art\\person.png')

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

    #Creating the first instance of the text box
    global html_nan 
    
    question_number =  str(results.question)
    print(texts)
    event_text_1 = pygame_gui.elements.ui_text_box.UITextBox(
        texts[question_number],
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

            #Clicking the buttons
            if event.type == MOUSEBUTTONDOWN:
                mouse_pos = event.pos # Now it will have the coordinates of click point.
                if yesButtonPosition.collidepoint(mouse_pos):
                    gui.response.yes_response(question_number, manager, texts)

                if noButtonPosition.collidepoint(mouse_pos):
                    gui.response.no_response(question_number, manager, texts)

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

mayorName = str(gui.playerInput.makeMayor())
cityName = str(gui.playerInput.makeCity())
texts = html_reader.read_file(mayorName,cityName)

run_game()