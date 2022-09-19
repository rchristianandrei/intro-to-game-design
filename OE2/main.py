import pygame

pygame.init()

window = pygame.display.set_mode((800, 600))
playing = True

pygame.display.set_caption("First Pygame")

x, y, width, height, speed = 415, 275, 50, 50, 0.3

x2, y2, width2, height2, speed2 = 335, 275, 50, 50, 0.3

while playing:
    window.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    if keys[pygame.K_a]:
        x2 -= speed
    if keys[pygame.K_d]:
        x2 += speed
    if keys[pygame.K_w]:
        y2 -= speed
    if keys[pygame.K_s]:
        y2 += speed

    pygame.draw.rect(window, (0, 255, 0), (x2, y2, width2, height2))
    pygame.draw.rect(window, (255, 255, 0), (x, y, width, height))
    pygame.display.update()

