import pygame
from object import Object


def move_shape(key, speed):
    if key:
        return speed
    return 0


def main():
    pygame.init()

    window = pygame.display.set_mode((800, 600))
    playing = True

    pygame.display.set_caption("First Pygame")

    object1 = Object(415, 275, 50, 50, (255, 255, 0))
    object2 = Object(335, 275, 50, 50, (0, 255, 0))

    while playing:
        window.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False

        keys = pygame.key.get_pressed()

        # Move Objects
        object1.x += move_shape(keys[pygame.K_LEFT], -Object.speed)
        object1.x += move_shape(keys[pygame.K_RIGHT], Object.speed)
        object1.y += move_shape(keys[pygame.K_UP], -Object.speed)
        object1.y += move_shape(keys[pygame.K_DOWN], Object.speed)

        object2.x += move_shape(keys[pygame.K_a], -Object.speed)
        object2.x += move_shape(keys[pygame.K_d], Object.speed)
        object2.y += move_shape(keys[pygame.K_w], -Object.speed)
        object2.y += move_shape(keys[pygame.K_s], Object.speed)

        # Draw Objects
        pygame.draw.rect(window, object1.color, (object1.x, object1.y, object1.w, object1.h))
        pygame.draw.rect(window, object2.color, (object2.x, object2.y, object2.w, object2.h))

        pygame.display.update()

    pygame.quit()


main()
