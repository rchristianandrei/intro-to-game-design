import pygame
from object import Object
from character import Character
from ninja import Ninja
from projectile import Projectile

# Window Settings
pygame.init()

width, height = 800, 600

Object.height = height
Object.width = width

window = pygame.display.set_mode((width, height))
playing = True

pygame.display.set_caption("First Pygame")

load = pygame.image.load
background = load("../images/bg.jpg")
background = pygame.transform.scale(background, (1278, 720))

# Clock
clock = pygame.time.Clock()

# Initialize Objects
projectiles = [Projectile(-100, 10, 32, 160)]
objects = [Ninja(415, 275, 77, 146, projectiles[0]), Character(415, 275, 117, 141)]

objects[0].idle_scale = (77, 146)
objects[0].run_scale = (110, 146)
objects[0].jump_scale = (110, 170)
objects[0].throw_scale = (130, 150)

objects[1].idle_scale = (117, 141)
objects[1].run_scale = (110, 146)
objects[1].jump_scale = (110, 140)

projectiles[0].scale = (16, 80)
projectiles[0].rotation = -90

# Assign Sprite Settings
projectiles[0].sprites = load('../images/object1/Kunai/Kunai.png')

for x in range(10):
    # Object0
    objects[0].IDLE.append(load(f'../images/object1/Idle/Idle__00{x}.png'))
    objects[0].RUN.append(load(f'../images/object1/Run/Run__00{x}.png'))
    objects[0].JUMP.append(load(f'../images/object1/Jump/Jump__00{x}.png'))
    objects[0].THROW.append(load(f'../images/object1/Throw/Throw__00{x}.png'))

    # Object1
    objects[1].IDLE.append(load(f'../images/object2/Idle/Idle ({x + 1}).png'))
    objects[1].RUN.append(load(f'../images/object2/Run/Run ({x + 1}).png'))
    objects[1].JUMP.append(load(f'../images/object2/Jump/Jump ({x + 1}).png'))

# Resize the sprites
for x in projectiles:
    x.resize_sprite()

for x in objects:
    x.resize_sprites()

# Game Loop
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

    keys = pygame.key.get_pressed()

    # Assign keys
    objects[0].moving = [
        keys[pygame.K_w],
        keys[pygame.K_s],
        keys[pygame.K_a],
        keys[pygame.K_d],
        keys[pygame.K_SPACE],
        keys[pygame.K_e]]
    objects[1].moving = [
        keys[pygame.K_UP],
        keys[pygame.K_DOWN],
        keys[pygame.K_LEFT],
        keys[pygame.K_RIGHT],
        keys[pygame.K_KP_0]]

    # Move & Draw Objects
    window.blit(background, (-239, -60))

    for x in projectiles:
        x.move()
        window.blit(x.active_sprite, (x.x, x.y))

    for x in objects:
        x.move()
        window.blit(x.active_sprite, (x.x, x.y))

    # Update
    pygame.display.update()
    clock.tick(60)
    Object.counter += 1
    if Object.counter > 999:
        Object.counter = 0

pygame.quit()
