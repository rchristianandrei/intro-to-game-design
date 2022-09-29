import pygame
from object import Object


def move_shape(key, cond, speed):
    if key and cond:
        return speed
    return 0


def east_bound(x, w, width):
    return x < width - (w + 10)


def south_bound(y, h, height):
    return y < height - (h + 10)


def main():
    pygame.init()

    width, height = 800, 600

    window = pygame.display.set_mode((800, 600))
    playing = True

    pygame.display.set_caption("First Pygame")

    object1 = Object(415, 275, 50, 50, (255, 255, 0))
    object2 = Object(335, 275, 50, 50, (0, 255, 0))

    north_bound, west_bound = 10, 10

    while playing:
        window.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False

        keys = pygame.key.get_pressed()

        # Move Objects

        object1.x += move_shape(keys[pygame.K_LEFT], object1.x > west_bound, -Object.speed)
        object1.x += move_shape(keys[pygame.K_RIGHT], east_bound(object1.x, object1.w, width), Object.speed)
        object1.y += move_shape(keys[pygame.K_UP], object1.y > north_bound, -Object.speed)
        object1.y += move_shape(keys[pygame.K_DOWN], south_bound(object1.y, object1.h, height), Object.speed)

        object2.x += move_shape(keys[pygame.K_a], object2.x > west_bound, -Object.speed)
        object2.x += move_shape(keys[pygame.K_d], east_bound(object2.x, object2.w, width), Object.speed)
        object2.y += move_shape(keys[pygame.K_w], object2.y > north_bound, -Object.speed)
        object2.y += move_shape(keys[pygame.K_s], south_bound(object2.y, object2.h, height), Object.speed)

        # Draw Objects
        pygame.draw.rect(window, object1.color, (object1.x, object1.y, object1.w, object1.h))
        pygame.draw.rect(window, object2.color, (object2.x, object2.y, object2.w, object2.h))

        pygame.display.update()

    pygame.quit()


main()
