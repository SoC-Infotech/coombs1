import pygame
import random

#Initialize the pygame (game loop, game scene)
pygame.init()

#Declare some variables/constants
winHeight = 480
winWidth = 700
GREEN = (0,255,0)

#Create window game
win = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption("Hangman by Sabian")

#Main program
#Create a game loop to keep the window visible
inPlay = True
while inPlay:
    #Use loop to draw window
    win.fill(GREEN) #Make background colour green
    pygame.display.update()
    pygame.time.delay(100)
    
    
#Quite the pygamepygame.quite()