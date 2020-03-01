import pygame
import pygame_gui
from pygame.rect import Rect

from gui import intro

from event_test.results import morale, population, diseased

pygame.init()

pygame.display.set_caption('Ending')

manager = pygame_gui.UIManager((800, 600))

white = (255,255,255)
hover = (191, 191, 191)  # color when hover on "return to title screen"

display_width = 800
display_height = 600

ourDisplay = pygame.display.set_mode((display_width,display_height))

# fonts to display
myfont = pygame.font.SysFont('Comic Sans MS', 50)
font2 = pygame.font.SysFont('Serif', 30)
score_font = pygame.font.SysFont('Serif', 20)
final_font = pygame.font.SysFont('Serif', 60)


# game over text
textSurface = myfont.render('GAME OVER!', False, white)
text2 = font2.render('evarywan s ded ur bad lol', False, white)



score = (population + morale) - diseased
scores = {"Population": population, "Diseased": diseased, "Morale": morale}
final_score = final_font.render("Score: " + str(score), False, (0, 153, 51))


ret_pos = (250, 500)

ret_position = Rect(220, 480, 400, 80)
ret_position.collidepoint(pygame.mouse.get_pos())


is_running = True
title = False
while is_running:

    ourDisplay.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if ret_position.collidepoint(mouse_pos):
                is_running = False
                title = True

    if ret_position.collidepoint(pygame.mouse.get_pos()):
        ret_text = font2.render('Return to Title Screen', False, hover)
        ourDisplay.blit(ret_text, ret_pos)
    else:
        ret_text = font2.render('Return to Title Screen', False, white)
        ourDisplay.blit(ret_text, ret_pos)

    ourDisplay.blit(textSurface, (250, 50))
    ourDisplay.blit(text2, (250, 110))

    # loop through text and display score variables
    score_level = 170
    for s in scores:
        score_text = score_font.render(s + ": " + str(scores[s]), False, white)
        ourDisplay.blit(score_text, (300, score_level))
        score_level += 25

    ourDisplay.blit(final_score, (250, score_level + 70))

    pygame.display.update()

if title:
    intro.game_intro()
