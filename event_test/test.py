

import pygame 
import pygame_gui


def run_game():
    pygame.init() 
    pygame.display.set_caption('Hello Gamers')
    win_sur = pygame.display.set_mode((800,600))
    
    br = pygame.Surface((800,600))
    br.fill(pygame.Color('#000f00'))

    manager = pygame_gui.UIManager((800, 600))

    clock = pygame.time.Clock()

    #gui button
    hello_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect(
            (350, 275),
            (100, 50)
        ),
        text='Say Hello',
        manager=manager
    )
    
    event_text_1 = pygame_gui.elements.ui_text_box.UITextBox(
                "<p>HI</p>",    
                relative_rect=pygame.Rect(
                    (200,175),
                    (150,100) 
                ),
                manager=manager 
            )
    

    is_running = True 

    while is_running: 
        time_delta = clock.tick(60)/1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            manager.process_events(event)

        win_sur.blit(br,(0,0))

        manager.draw_ui(win_sur)

        pygame.display.update()


run_game()

