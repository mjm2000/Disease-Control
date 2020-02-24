import pygame
from pygame.locals import *


def game_intro():
    intro = True
    clock = pygame.time.Clock()
    display_width = 800
    display_height = 600
    ourDisplay = pygame.display.set_mode((display_width,display_height))
    myfont = pygame.font.SysFont('Comic Sans MS', 40)
    white =(255,255,255)
    exitImg = pygame.image.load('art\\exitButton.png')
    playImg = pygame.image.load('art\\startButton.png')

    playImgPosition = Rect(100,0,0,400)
    playImgPosition.collidepoint(pygame.mouse.get_pos())
    playImgPosition = playImg.get_rect()
    playImgPosition = playImgPosition.move(275,350)

    exitImgPosition = Rect(200,0,0,500)
    exitImgPosition.collidepoint(pygame.mouse.get_pos())
    exitImgPosition = exitImg.get_rect()
    exitImgPosition = exitImgPosition.move(275,450)


    background = pygame.image.load('art\\titleScreen.png')

    while intro:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                mouse_pos = event.pos # Now it will have the coordinates of click point.
                if playImgPosition.collidepoint(mouse_pos):
                    ourDisplay.blit(background,(0,0))
                    intro = False
                if exitImgPosition.collidepoint(mouse_pos):
                    ourDisplay.blit(background,(0,0))
                    exit()

        ourDisplay.blit(background,(0,0))
        textsurface = myfont.render('Disease Control', False,white)

        ourDisplay.blit(background,(0,0))
        ourDisplay.blit(textsurface,(250,0))
        ourDisplay.blit(playImg, playImgPosition)
        ourDisplay.blit(exitImg, exitImgPosition)
        pygame.display.update()
        clock.tick(15)