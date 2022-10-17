import copy
import pygame


class Object:
    speed = 4
    jump_force = -100
    north_bound, west_bound = 10, 10
    width = None
    height = None
    scale = (77, 146)
    counter = 1

    @staticmethod
    def move_shape(key, cond, speed):
        if key and cond:
            return speed
        return 0

    @staticmethod
    def south_bound(y, h, height):
        return y < height - (h + 10)

    @staticmethod
    def east_bound(x, w, width):
        return x < width - (w + 10)

    def __init__(self, x, y, w, h):

        # Primary Settings
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.flip = None

