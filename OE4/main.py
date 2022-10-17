import pygame
from object import Object


def main():
    pygame.init()

    width, height = 800, 600

    Object.height = height
    Object.width = width

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

        object1.moving = [
            keys[pygame.K_UP],
            keys[pygame.K_DOWN],
            keys[pygame.K_LEFT],
            keys[pygame.K_RIGHT],
            keys[pygame.K_KP_0]]
        object2.moving = [
            keys[pygame.K_w],
            keys[pygame.K_s],
            keys[pygame.K_a],
            keys[pygame.K_d],
            keys[pygame.K_SPACE]]

        # Move Objects
        object1.move()
        object2.move()

        # Draw Objects
        pygame.draw.rect(window, object1.color, (object1.x, object1.y, object1.w, object1.h))
        pygame.draw.rect(window, object2.color, (object2.x, object2.y, object2.w, object2.h))

        pygame.display.update()

    pygame.quit()


main()
