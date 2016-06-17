from constants import *

import pygame


class FuelTank:
    def __init__(self, tank_id):
        self.texture = pygame.image.load(TANK_TEXTURE[tank_id])

        self.mass = TANK_MASS[tank_id]
        self.fuel = TANK_FUEL[tank_id]

    def deplete_fuel(self, decrement):
        if self.fuel - decrement < 0:
            self.fuel = 0
        else:
            self.fuel -= decrement
