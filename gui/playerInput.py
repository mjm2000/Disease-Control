#Creating mayor
import pygame
import gui.pygame_textinput
import gui.intro


ourDisplay = pygame.display.set_mode((800, 600))
running = True
runningAgain = True
background = pygame.image.load('art\\titleScreen.png')
global mayor, city

# Create TextInput-object
textinput = gui.pygame_textinput.TextInput()
def message_display(text):
    largeText = pygame.font.Font('fonts\\OrthodoxHerbertarian.ttf',40)
    TextSurf, TextRect = text_main(text, largeText)
    TextRect.center = ((400),(400))
    ourDisplay.blit(TextSurf, TextRect)
def text_main(text, font):
    black = (255,255,255)
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
def makeMayor():
    while running:
        ourDisplay.blit(background,(0,0))
        events = pygame.event.get()
        message_display('Enter name of your mayor')
        for event in events:
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    mayor = textinput.input_string
                    textinput.input_string = ""
                    return mayor
        # Feed it with events every frame
        textinput.update(events)
        # Blit its surface onto the screen
        ourDisplay.blit(textinput.get_surface(), (350, 500))
        pygame.display.update()

def makeCity():
    while runningAgain:
        ourDisplay.blit(background,(0,0))
        events = pygame.event.get()
        message_display('Enter a name for your city')
        for event in events:
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    city = textinput.input_string
                    textinput.input_string = ""
                    return city
        # Feed it with events every frame
        textinput.update(events)
        # Blit its surface onto the screen
        ourDisplay.blit(textinput.get_surface(), (350, 500))
        pygame.display.update()
