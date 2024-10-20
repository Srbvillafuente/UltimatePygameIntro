import pygame 
from sys import exit

pygame.init()
screen= pygame.display.set_mode((800,400))
# makes a screen for the 'game', this is a touple and has width, height

pygame.display.set_caption('Runner')
# sets title for the display/game

clock = pygame.time.Clock()
# This gives a clock object

test_surface = pygame.image.load('graphics/Sky.png')


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #this is basically the closing of the window
            pygame.quit()
            exit()

    screen.blit(test_surface,(200,100))

    # draws all our elements and updates everything
    pygame.display.update() 
    clock.tick(60) 
