
import pygame
import pygame_gui

texts = [
    "<b>A man has fallen into the river in lego city!</b>",
    "<b>Build the new rescue helicopter!</b>",
    "<b>HEY!!</b>"
]

# def run_game():
#     pygame.init()
#     pygame.display.set_caption('Hello Gamers')
#     win_sur = pygame.display.set_mode((800,600))
#
#     br = pygame.Surface((800,600))
#
#     manager = pygame_gui.UIManager((800, 600))
#
#     clock = pygame.time.Clock()
#
#     #gui button
#     hello_button = pygame_gui.elements.UIButton(
#         relative_rect=pygame.Rect(
#             (350, 275),
#             (100, 50)
#         ),
#         text='Say Hello',
#         manager=manager
#     )
#     text_index = 0
#
#     #this is the text box
#     event_text_1 = pygame_gui.elements.ui_text_box.UITextBox(
#         texts[text_index],
#         relative_rect=pygame.Rect(
#             (170,120),
#             (500,150)
#         ),
#         manager=manager
#     )
#
#     is_running = True
#
#     while is_running:
#         #need to keep track of mouse position
#         mouse = pygame.mouse.get_pos()
#
#         time_delta = clock.tick(60)/1000.0
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 is_running = False
#             manager.process_events(event)
#
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_h:
#                     text_index += 1
#                     event_text_1 = pygame_gui.elements.ui_text_box.UITextBox(
#                         texts[text_index],
#                         relative_rect=pygame.Rect(
#                             (170,120),
#                             (500,150)
#                         ),
#                         manager=manager
#                     )
#
#         win_sur.blit(br,(0,0))
#
#         manager.draw_ui(win_sur)
#
#         pygame.display.update()
#
#
# run_game()

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

    #this is the text box
    text_index = 0

    event_text_1 = pygame_gui.elements.ui_text_box.UITextBox(
        'hello',
        relative_rect=pygame.Rect(
            (170,120),
            (500,150)
        ),
        manager=manager
    )


    is_running = True

    while is_running:
        ourDisplay.fill(white)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

            #press key to change text
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_h:
                    text_index += 1
                    event_text_1 = pygame_gui.elements.ui_text_box.UITextBox(
                        texts[text_index],
                        relative_rect=pygame.Rect(
                            (170,120),
                            (500,150)
                        ),
                        manager=manager
                    )
            manager.process_events(event)
        yesButton(0,400)
        black = (0,0,0)
        manager.draw_ui(ourDisplay)
        pygame.draw.rect(ourDisplay,black,(600,0,700,600))
        sideBar(625,0)
        noButton(300,400)
        pygame.display.update()

run_game()
