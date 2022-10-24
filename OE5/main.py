import pygame

pygame.init()

width = 1100
height = 700
title = "Andrei's Game"

window = pygame.display.set_mode((width, height))
pygame.display.set_caption(title)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

pygame.quit()
