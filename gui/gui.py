
import pygame
import pygame_gui


def run_game():
    pygame.init()
    pygame.display.set_caption('Disease Control')
    display_width = 800
    display_height = 600
    white = (255,255,255)
    ourDisplay = pygame.display.set_mode((display_width,display_height))

    br = pygame.Surface((800,600))

    manager = pygame_gui.UIManager((800, 600))


    hello_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect(
            (0,400),
            (300, 300)
        ),
        text="hey gamers",
        manager=manager
    )
    yesButtonImg = pygame.image.load('yes3.png')
    noButtonImg = pygame.image.load('nooo.png')

    def yesButton(x,y):
        ourDisplay.blit(yesButtonImg, (x, y))


    def noButton(x,y):
        ourDisplay.blit(noButtonImg, (x, y))

    is_running = True
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            manager.process_events(event)
        ourDisplay.fill(white)
        noButton(300,400)
        yesButton(0,400)




        pygame.display.update()


run_game()
