import pygame

# Initisialize the pygame
pygame.init()

# Create the screen/windows
screen = pygame.display.set_mode((800, 600))
running = True

# Gaming loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False