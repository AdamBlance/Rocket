from constants import *
from FuelTank import FuelTank
from Engine import Engine

import pygame
from pygame.locals import *


class Ship(pygame.Surface):
    all_tanks = []
    all_engines = []

    def __init__(self, parts):
        ship_height = 0
        for part in parts:
            if isinstance(part, FuelTank):
                self.all_tanks.append(part)
            elif isinstance(part, Engine):
                self.all_engines.append(part)

            ship_height += part.texture.get_rect().height

        self.total_mass = self.get_total_mass()

        self.x = (RESOLUTION[0]/2) - 25
        self.y = RESOLUTION[1] - ship_height
        self.dx = 0
        self.dy = 0

        self.throttle = 0
        self.bearing = 0

        self.texture = None  # Added because I can't set self to a Surface object.
        super(Ship, self).__init__((50, ship_height), SRCALPHA)

        offset = 0
        for part in parts:
            self.blit(part.texture, (0, offset))
            offset += part.texture.get_rect().height

    def move(self):
        self.dx += self.get_horizontal_acceleration()
        self.dy += self.get_vertical_acceleration(GRAVITY['EARTH'])
        self.x += self.dx
        self.y -= self.dy

        self.texture = pygame.transform.rotate(self, -self.bearing)

    def use_fuel(self):
        for tank in self.all_tanks:
            if tank.fuel > 0:
                tank.deplete_fuel(self.get_fuel_consumption())
                continue

    def set_throttle_to(self, value):
        if 1 >= value >= 0:
            self.throttle = value

    def change_throttle_by(self, value):
        if 1 >= self.throttle + value >= 0:
            self.throttle += value
        else:
            if self.throttle + value > 1:
                self.throttle = 1
            else:
                self.throttle = 0

    def change_bearing_by(self, degrees):
        self.bearing = (degrees + self.bearing) % 360

    def get_fuel_consumption(self):
        fuel_consumption = 0
        for engine in self.all_engines:
            fuel_consumption += engine.max_consumption
        fuel_consumption = (fuel_consumption * self.throttle)/MAX_FPS
        return fuel_consumption

    def get_total_fuel(self):
        total_fuel = 0
        for tank in self.all_tanks:
            total_fuel += tank.fuel
        return total_fuel

    def get_total_mass(self):
        total_mass = 0
        for tank in self.all_tanks:
            total_mass += (tank.fuel * FUEL_MASS) + tank.mass
        for engine in self.all_engines:
            total_mass += engine.mass
        return total_mass

    def get_vertical_acceleration(self, gravity):
        mass = self.get_total_mass()
        total_vertical_force = mass * gravity
        if self.get_total_fuel() > 0:
            for engine in self.all_engines:
                total_vertical_force += engine.get_vertical_force(self.bearing, self.throttle)

        acceleration = total_vertical_force/mass
        return acceleration/MAX_FPS

    def get_horizontal_acceleration(self):
        total_horizontal_force = 0
        mass = self.get_total_mass()
        for engine in self.all_engines:
            total_horizontal_force += engine.get_horizontal_force(self.bearing, self.throttle)

        acceleration = total_horizontal_force/mass
        return acceleration/MAX_FPS
