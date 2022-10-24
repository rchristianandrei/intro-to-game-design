from character import Character
from animation import Animation
from object import Object
import pygame

pygame.init()

# Window Settings
width = 1100
height = 700
title = "Andrei's Game"

window = pygame.display.set_mode((width, height))
pygame.display.set_caption(title)

# Game Settings
Object.width = width
Object.height = height

# Clock
clock = pygame.time.Clock()

# Game Objects
characters = [Character(width/2, height/2, 90, 121, 4)]
characters[0].IDLE.scale = (77, 146)
characters[0].IDLE.modulus = 4
characters[0].RUN.scale = (110, 146)
characters[0].RUN.modulus = 4
characters[0].JUMP.scale = (110, 170)
characters[0].JUMP.modulus = 4

# Sprites
for x in range(10):
    characters[0].IDLE.sprites.append(pygame.image.load(f'../images/object1/Idle/Idle__00{x}.png'))
    characters[0].RUN.sprites.append(pygame.image.load(f'../images/object1/Run/Run__00{x}.png'))
    characters[0].JUMP.sprites.append(pygame.image.load(f'../images/object1/Jump/Jump__00{x}.png'))

for x in characters:
    x.IDLE.resize()
    x.RUN.resize()
    x.JUMP.resize()

# Game Loop
running = True
while running:

    # Check Events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

    # Check Input
    keys = pygame.key.get_pressed()

    characters[0].hotkey = [keys[pygame.K_w],
                            keys[pygame.K_s],
                            keys[pygame.K_a],
                            keys[pygame.K_d],
                            keys[pygame.K_SPACE]]

    # Update Display
    window.fill((0, 0, 0))

    for x in characters:
        x.update()

        window.blit(x.active_sprite, (x.actual_x(), x.actual_y()))

    pygame.display.update()
    clock.tick(60)

    # Update Animation Counter
    if Animation.global_counter > Animation.counter_limit:
        Animation.global_counter = 0
    else:
        Animation.global_counter += 1

pygame.quit()
