
#these are the texts for the sidebar
import pygame

pygame.init()
white = (255,255,255)

display_width = 800
display_height = 600
ourDisplay = pygame.display.set_mode((display_width,display_height))
myfont = pygame.font.SysFont('Comic Sans MS', 20)

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
