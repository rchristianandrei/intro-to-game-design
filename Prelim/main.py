import pygame
from object import Object


def main():
    pygame.init()

    width, height = 800, 600

    Object.height = height
    Object.width = width

    window = pygame.display.set_mode((width, height))
    playing = True

    pygame.display.set_caption("First Pygame")

    # Clock
    clock = pygame.time.Clock()

    # Initialize Objects
    object1 = Object(415, 275, Object.scale[0], Object.scale[1], (255, 255, 0))
    #object2 = Object(335, 275, 50, 50, (0, 255, 0))

    load = pygame.image.load

    # Assign Sprite Settings
    object1.IDLE = [load('../images/object1/Idle/Idle__000.png'),
                    load('../images/object1/Idle/Idle__001.png'),
                    load('../images/object1/Idle/Idle__002.png'),
                    load('../images/object1/Idle/Idle__003.png'),
                    load('../images/object1/Idle/Idle__004.png'),
                    load('../images/object1/Idle/Idle__005.png'),
                    load('../images/object1/Idle/Idle__006.png'),
                    load('../images/object1/Idle/Idle__007.png'),
                    load('../images/object1/Idle/Idle__008.png'),
                    load('../images/object1/Idle/Idle__009.png')]
    object1.RUN = [load('../images/object1/Run/Run__000.png'),
                   load('../images/object1/Run/Run__001.png'),
                   load('../images/object1/Run/Run__002.png'),
                   load('../images/object1/Run/Run__003.png'),
                   load('../images/object1/Run/Run__004.png'),
                   load('../images/object1/Run/Run__005.png'),
                   load('../images/object1/Run/Run__006.png'),
                   load('../images/object1/Run/Run__007.png'),
                   load('../images/object1/Run/Run__008.png'),
                   load('../images/object1/Run/Run__009.png')]

    for x in range(len(object1.IDLE)):
        object1.IDLE[x] = pygame.transform.scale(object1.IDLE[x], (77, 146))

    for x in range(len(object1.RUN)):
        object1.RUN[x] = pygame.transform.scale(object1.RUN[x], (110, 146))

    while playing:
        window.fill((0, 0, 0))

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
            keys[pygame.K_SPACE]
        ]
        '''object2.moving = [
            keys[pygame.K_UP],
            keys[pygame.K_DOWN],
            keys[pygame.K_LEFT],
            keys[pygame.K_RIGHT],
            keys[pygame.K_KP_0]]'''

        # Move Objects
        object1.move()
        #object2.move()

        # Draw Objects
        #pygame.draw.rect(window, object1.color, (object1.x, object1.y, object1.w, object1.h))
        #pygame.draw.rect(window, object2.color, (object2.x, object2.y, object2.w, object2.h))

        window.blit(object1.active_sprite, (object1.x, object1.y, object1.w, object1.h))

        pygame.display.update()
        clock.tick(60)
        Object.counter += 1
        if Object.counter > 9:
            Object.counter = 0

    pygame.quit()


main()
