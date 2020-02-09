# import pygame
# import pygame_gui
# import gui.sideBar
# from pygame.locals import *
# from event_test import results
#
# def game_intro():
#
#     intro = True
#     clock = pygame.time.Clock()
#     display_width = 800
#     display_height = 600
#     ourDisplay = pygame.display.set_mode((display_width,display_height))
#     myfont = pygame.font.SysFont('Comic Sans MS', 40)
#     white =(255,255,255)
#     exitImg = pygame.image.load('exitButton.png')
#     playImg = pygame.image.load('startButton.png')
#
#     playImgPosition = Rect(100,0,0,400)
#     playImgPosition.collidepoint(pygame.mouse.get_pos())
#     playImgPosition = playImg.get_rect()
#     playImgPosition = playImgPosition.move(275,350)
#
#     exitImgPosition = Rect(200,0,0,500)
#     exitImgPosition.collidepoint(pygame.mouse.get_pos())
#     exitImgPosition = exitImg.get_rect()
#     exitImgPosition = exitImgPosition.move(275,450)
#
#
#     background = pygame.image.load('titleScreen.png')
#
#     while intro:
#         for event in pygame.event.get():
#             if event.type == MOUSEBUTTONDOWN:
#                 mouse_pos = event.pos # Now it will have the coordinates of click point.
#                 if playImgPosition.collidepoint(mouse_pos):
#                     intro = False
#                 if exitImgPosition.collidepoint(mouse_pos):
#                     exit()
#
#         ourDisplay.blit(background,(0,0))
#         #TextSurf, TextRect = text_objects('Disease Control', largeText)
#         textsurface = myfont.render('Disease Control', False,white)
#         #text_rect = TextRect.get_rect(center=(display_width/2, display_height))
#
#         ourDisplay.blit(textsurface,(250,0))
#         ourDisplay.blit(playImg, playImgPosition)
#         ourDisplay.blit(exitImg, exitImgPosition)
#         pygame.display.update()
#         clock.tick(15)