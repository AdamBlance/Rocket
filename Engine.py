from constants import *

import math
import pygame


class Engine:
    def __init__(self, engine_id):
        self.texture = pygame.image.load(ENGINE_TEXTURE[engine_id])

        self.max_thrust = ENGINE_THRUST_ATM[engine_id]
        self.max_consumption = ENGINE_CONSUMPTION[engine_id]
        self.mass = ENGINE_MASS[engine_id]

    def get_vertical_force(self, rotation, throttle):
        vertical_force = throttle * self.max_thrust * math.cos(math.radians(rotation))
        return vertical_force

    def get_horizontal_force(self, rotation, throttle):
        horizontal_force = throttle * self.max_thrust * math.sin(math.radians(rotation))
        return horizontal_force
