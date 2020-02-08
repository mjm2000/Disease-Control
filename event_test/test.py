import pygame
import pygame_gui

texts = [
            "<b>A man has fallen into the river in lego city!</b>",
            "<b>Build the new rescue helicopter!</b>",
            "<b>HEY!!</b>"
        ]

def run_game():
    pygame.init() 
    pygame.display.set_caption('Hello Gamers')
    win_sur = pygame.display.set_mode((800,600))
    
    br = pygame.Surface((800,600))

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
    text_index = 0

    #this is the text box
    event_text_1 = pygame_gui.elements.ui_text_box.UITextBox(
        texts[text_index],
        relative_rect=pygame.Rect(
            (170,120),
            (500,150)
        ),
        manager=manager
    )

    is_running = True 

    while is_running:
        #need to keep track of mouse position
        mouse = pygame.mouse.get_pos()

        time_delta = clock.tick(60)/1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            manager.process_events(event)

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

        win_sur.blit(br,(0,0))

        manager.draw_ui(win_sur)

        pygame.display.update()


run_game()

