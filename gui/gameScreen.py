
import pygame
import pygame_gui
import gui.sideBar
from pygame.locals import *

#this is just some dummy data
texts = [
    {"<p>A man has fallen into the river in lego city!</p>",
    "<p>Start the new rescue helicopter!</p>",
    "<p>HEY!!</p>",
    "<p>Build the helicopter and off to the rescue!</p>"
    "<p>Prepare the lifeline!</p>",
    "<p>Lower the stretcher!</p>",
    "<p>And make the rescue!</p>"
]


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
    increasingarrowImg = pygame.image.load('upvote.png')

    #These two methods create a yes and a no button
    def yesButton(x,y):
        yesButtonPosition = Rect(0,x,0,y)
        yesButtonPosition.collidepoint(pygame.mouse.get_pos())
        yesButtonPosition = yesButtonImg.get_rect()
        yesButtonPosition = yesButtonPosition.move(x,y)

        #Hover
        if yesButtonPosition.collidepoint(pygame.mouse.get_pos()):
            ourDisplay.blit(yesButtonHover, yesButtonPosition)
        else:
            ourDisplay.blit(yesButtonImg,yesButtonPosition)

        #Click
        if event.type == MOUSEBUTTONDOWN:
            mouse_pos = event.pos # Now it will have the coordinates of click point.
            if yesButtonPosition.collidepoint(mouse_pos):
                print("yes")

        #TODO Clickable Button changes button when clicked

    def noButton(x,y):
        noButtonPosition = Rect(0,x,0,y)
        noButtonPosition.collidepoint(pygame.mouse.get_pos())
        noButtonPosition = noButtonImg.get_rect()
        noButtonPosition = noButtonPosition.move(x,y)

        #Hover
        if noButtonPosition.collidepoint(pygame.mouse.get_pos()):
            ourDisplay.blit(noButtonImgHover, noButtonPosition)
        else:
            ourDisplay.blit(noButtonImg,noButtonPosition)

        if event.type == MOUSEBUTTONDOWN:
            mouse_pos = event.pos # Now it will have the coordinates of click point.
            if noButtonPosition.collidepoint(mouse_pos):
                print("no")
        #TODO Clickable Button changes button when clicked
    def downarrow(x, y):
        ourDisplay.blit(decreasearrowImg, (x + 20, y))

    def uparrow(x, y):
        ourDisplay.blit(increasingarrowImg, (x + 80, y))

    #these are the texts for the sidebar
    myfont = pygame.font.SysFont('Comic Sans MS', 20)


    #this is the text box
    text_index = 0

    event_text_1 = pygame_gui.elements.ui_text_box.UITextBox(
        texts[text_index],
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
            manager.process_events(event)
        black = (0,0,0)
        ourDisplay.fill(black)
        ourDisplay.blit(backgroundImage,(0,0))
        yesButton(0,400)
        pygame.draw.rect(ourDisplay,black,(600,0,700,600))
        gui.sideBar.weektitle(660,70)
        gui.sideBar.weekvariable(730, 70, "1")

        # should be 30 away from its corresponding variable
        # the 3rd argument is the variable
        gui.sideBar.totalpoptitle(625, 180)
        gui.sideBar.totalpopvariable(700, 210, "%")

        gui.sideBar.diseasedtitle(625, 300)
        gui.sideBar.diseasedvariable(700, 330, "%")

        gui.sideBar.moraletitle(660, 420)
        gui.sideBar.moralevariable(700, 450, "%")
        noButton(300,400)

        #draws the textbox
        manager.draw_ui(ourDisplay)

        pygame.display.update()

run_game()

















