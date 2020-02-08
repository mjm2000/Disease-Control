
import pygame
import pygame_gui
from pygame.locals import *


def run_game():
    pygame.init()
    pygame.display.set_caption('Disease Control')

    white = (255,255,255)

    display_width = 800
    display_height = 600
    ourDisplay = pygame.display.set_mode((display_width,display_height))

    manager = pygame_gui.UIManager((800, 600))

    #Load Images
    yesButtonImg = pygame.image.load('yes3.png')
    noButtonImg = pygame.image.load('nooo.png')

    #These two methods create a yes and a no button
    def yesButton(x,y):
        yesButtonPosition = Rect(0,x,0,y)
        yesButtonPosition.collidepoint(pygame.mouse.get_pos())
        yesButtonPosition = yesButtonImg.get_rect()
        yesButtonPosition = yesButtonPosition.move(x,y)
        ourDisplay.blit(yesButtonImg, yesButtonPosition)

        if event.type == MOUSEBUTTONDOWN:
            mouse_pos = event.pos # Now it will have the coordinates of click point.
            if yesButtonPosition.collidepoint(mouse_pos):
                print('LETS GO GAMERS')
        #TODO Highlight Button on hover
        #TODO Clickable Button changes button when clicked

    def noButton(x,y):
        ourDisplay.blit(noButtonImg, (x, y))
        #TODO Highlight Button on hover
        #TODO Clickable Button changes button when clicked

    #these are the texts for the sidebar
    myfont = pygame.font.SysFont('Comic Sans MS', 20)
    textsurface = myfont.render('Total Population', False, (255, 255, 255))

    def sideBar(x,y):
        textSurface = myfont.render('Total Population', False, (255, 255, 255))
        ourDisplay.blit(textsurface,(x,y))

    is_running = True
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            manager.process_events(event)
        ourDisplay.fill(white)
        yesButton(0,400)
        black = (0,0,0)
        pygame.draw.rect(ourDisplay,black,(600,0,700,600))
        sideBar(625,0)
        noButton(300,400)
        pygame.display.update()

run_game()

















