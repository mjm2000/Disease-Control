
import pygame
import pygame_gui
import gui.sideBar
from pygame.locals import *



pygame.init()
white = (255,255,255)

display_width = 800
display_height = 600
ourDisplay = pygame.display.set_mode((display_width,display_height))
myfont = pygame.font.SysFont('Comic Sans MS', 20)
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