import pygame


def move_shape(key, speed):
    if key:
        return speed
    return 0


def main():
    pygame.init()

    window = pygame.display.set_mode((800, 600))
    playing = True

    pygame.display.set_caption("First Pygame")

    x, y, width, height, speed, color = 415, 275, 50, 50, 0.3, (255, 255, 0)
    x2, y2, width2, height2, speed2, color2 = 335, 275, 50, 50, 0.3, (0, 255, 0)

    while playing:
        window.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False

        keys = pygame.key.get_pressed()

        # Move Objects
        x += move_shape(keys[pygame.K_LEFT], -speed)
        x += move_shape(keys[pygame.K_RIGHT], speed)
        y += move_shape(keys[pygame.K_UP], -speed)
        y += move_shape(keys[pygame.K_DOWN], speed)

        x2 += move_shape(keys[pygame.K_a], -speed)
        x2 += move_shape(keys[pygame.K_d], speed)
        y2 += move_shape(keys[pygame.K_w], -speed)
        y2 += move_shape(keys[pygame.K_s], speed)

        # Draw Objects
        pygame.draw.rect(window, color, (x, y, width, height))
        pygame.draw.rect(window, color2, (x2, y2, width2, height2))

        pygame.display.update()

    pygame.quit()


main()
