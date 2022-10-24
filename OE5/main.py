from projectile import Projectile
from animation import Animation
from object import Object
from enemy import Enemy
from ninja import Ninja
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
background = pygame.image.load('../images/bg2.png')
projectiles = [Projectile(width*2, height/2, 80, 16, 10)]
characters = [Ninja(width/2, height/2, 90, 121, 4, projectiles[0])]
enemies = [Enemy(width/2, height - 200, 227, 157, 2)]

characters[0].IDLE.scale = (77, 146)
characters[0].IDLE.modulus = 4
characters[0].RUN.scale = (110, 146)
characters[0].RUN.modulus = 4
characters[0].JUMP.scale = (110, 170)
characters[0].JUMP.modulus = 5
characters[0].THROW.scale = (130, 150)
characters[0].THROW.modulus = 4

enemies[0].RUN.scale = (227, 157)
enemies[0].RUN.modulus = 4

projectiles[0].set_owner(characters[0])

# Sprites
projectiles[0].sprite.sprites.append(pygame.image.load('../images/object1/Kunai/Kunai.png'))
projectiles[0].sprite.sprites = [pygame.transform.rotate(projectiles[0].sprite.sprites[0], -90)]

for x in range(10):
    characters[0].IDLE.sprites.append(pygame.image.load(f'../images/object1/Idle/Idle__00{x}.png'))
    characters[0].RUN.sprites.append(pygame.image.load(f'../images/object1/Run/Run__00{x}.png'))
    characters[0].JUMP.sprites.append(pygame.image.load(f'../images/object1/Jump/Jump__00{x}.png'))
    characters[0].THROW.sprites.append(pygame.image.load(f'../images/object1/Throw/Throw__00{x}.png'))

    enemies[0].RUN.sprites.append(pygame.image.load(f'../images/dinosaur/walk/Walk ({x+1}).png'))

for x in characters:
    x.IDLE.resize()
    x.RUN.resize()
    x.JUMP.resize()
    x.THROW.resize()

for x in projectiles:
    x.sprite.resize()

for x in enemies:
    x.RUN.resize()

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
                            keys[pygame.K_SPACE],
                            keys[pygame.K_e]]

    # Update Display
    window.blit(background, (0, -300))

    for x in enemies:
        x.update()

        window.blit(x.active_sprite, (x.actual_x(), x .actual_y()))

    for x in characters:
        x.update()

        window.blit(x.active_sprite, (x.actual_x(), x.actual_y()))

    for x in projectiles:
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
