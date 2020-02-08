
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
    noButtonImg = pygame.image.load('redButton.png')
    noButtonImgHover = pygame.image.load('redButtonHover.png')

    yesButtonImg = pygame.image.load('greenButtonwoop.png')
    yesButtonHover = pygame.image.load('greenButton.png')

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

        #TODO Highlight Button on hover
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
        #TODO Highlight Button on hover
        #TODO Clickable Button changes button when clicked

    #these are the texts for the sidebar
    myfont = pygame.font.SysFont('Comic Sans MS', 20)
    textsurface = myfont.render('Total Population', False, (255, 255, 255))

    def weektitle(x, y):
        textsurface = myfont.render('Week:', False, (255, 255, 255))
        ourDisplay.blit(textsurface, (x, y))

    def weekvariable(x, y, text):
        textsurface = myfont.render(text, False, (255, 255, 255))
        ourDisplay.blit(textsurface, (x, y))

    def totalpoptitle(x, y):
        textsurface = myfont.render('Total Population', False, (255, 255, 255))
        ourDisplay.blit(textsurface, (x, y))

    def totalpopvariable(x, y, text):
        # this is only going to do strings so maybe think about a converter so
        # it can change int to string and back and forth
        textsurface = myfont.render(text, False, (255, 255, 255))
        ourDisplay.blit(textsurface, (x, y))

    def diseasedtitle(x, y):
        textsurface = myfont.render("Total Diseased", False, (255, 255, 255))
        ourDisplay.blit(textsurface, (x, y))

    def diseasedvariable(x, y, text):
        textsurface = myfont.render(text, False, (255, 255, 255))
        ourDisplay.blit(textsurface, (x, y))

    def moraletitle(x, y):
        textsurface = myfont.render("Morale", False, (255, 255, 255))
        ourDisplay.blit(textsurface, (x, y))

    def moralevariable(x, y, text):
        # this is only going to do strings so maybe think about a converter so it can change int to string and back and forth
        textsurface = myfont.render(text, False, (255, 255, 255))
        ourDisplay.blit(textsurface, (x, y))

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
        weektitle(660, 70)
        weekvariable(730, 70, "1")

        # should be 30 away from its corresponding variable
        # the 3rd argument is the variable
        totalpoptitle(625, 180)
        totalpopvariable(700, 210, "%")

        diseasedtitle(625, 300)
        diseasedvariable(700, 330, "%")

        moraletitle(660, 420)
        moralevariable(700, 450, "%")
        noButton(300,400)
        pygame.display.update()

run_game()

















