import pygame
from object import Object


def main():
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
    object1 = Object(415, 275)
    object1.idle_scale = (77, 146)
    object1.run_scale = (110, 146)
    object1.jump_scale = (110, 170)
    object1.w = 77
    object1.h = 146

    # Assign Sprite Settings
    for x in range(10):
        object1.IDLE.append(load(f'../images/object1/Idle/Idle__00{x}.png'))

    for x in range(10):
        object1.RUN.append(load(f'../images/object1/Run/Run__00{x}.png'))

    for x in range(10):
        object1.JUMP.append(load(f'../images/object1/Jump/Jump__00{x}.png'))

    object1.resize_sprites()

    while playing:
        window.fill((0, 0, 0))
        window.blit(background, (-239, -60))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False

        keys = pygame.key.get_pressed()

        # Assign keys
        object1.moving = [
            keys[pygame.K_w],
            keys[pygame.K_s],
            keys[pygame.K_a],
            keys[pygame.K_d],
            keys[pygame.K_SPACE]]

        # Move Objects
        object1.move()

        # Draw Objects
        window.blit(object1.active_sprite, (object1.x, object1.y, object1.w, object1.h))

        # Update
        pygame.display.update()
        clock.tick(60)
        Object.counter += 1
        if Object.counter > 999:
            Object.counter = 0

    pygame.quit()


main()
