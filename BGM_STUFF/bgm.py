import sys
import pygame
from pygame.locals import *

def main():
    #Initialize Everything
    pygame.init()
    pygame.font.init()

    #Setting up Everything
    size = (1191,670)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Snowball Frontier')
    bg = pygame.image.load("ignite.png")

    #Play Music
    pygame.mixer.music.load('CrimsonBlitz.mp3')
    pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
    pygame.mixer.music.play(-1)

    #Blit to Screen
    screen.blit(bg, (0,0))

    

    #Event
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        
main()
