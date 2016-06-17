"""
Engine thrust is in N
Engine/tank mass is in Kg
Tank fuel is in l
Fuel mass is in Kg/l
Fuel consumption in l/s
Ship acceleration in px/tick
"""

from constants import *
from Engine import Engine
from FuelTank import FuelTank
from Controller import Controller
from Ship import Ship
from Stats import Stats

import pygame
from pygame.locals import *

main_surface = pygame.display.set_mode(RESOLUTION)

keyboard = Controller()

test_fuel_tank_1 = FuelTank('small_tank')
test_fuel_tank_2 = FuelTank('medium_tank')
test_engine = Engine('basic_engine')
test_ship = Ship([test_fuel_tank_1, test_fuel_tank_2, test_engine])

stats = Stats(test_ship)

clock = pygame.time.Clock()
running = True
while running:

    main_surface.fill([255, 255, 255])

    clock.tick(MAX_FPS)
    keyboard.update()

    if keyboard.exit:
        running = False
    if K_LSHIFT in keyboard.pressed_keys:
        test_ship.change_throttle_by(1/90)
    if K_LCTRL in keyboard.pressed_keys:
        test_ship.change_throttle_by(-1/90)
    if K_x in keyboard.pressed_keys:
        test_ship.set_throttle(0)
    if K_z in keyboard.pressed_keys:
        test_ship.set_throttle(1)
    if K_s in keyboard.pressed_keys:
        test_ship.change_bearing_by(1)
    if K_a in keyboard.pressed_keys:
        test_ship.change_bearing_by(-1)

    test_ship.move(test_ship.get_horizontal_acceleration(test_ship.get_total_mass()),
                   test_ship.get_vertical_acceleration(test_ship.get_total_mass(), GRAVITY['EARTH']))
    test_ship.use_fuel(test_ship.get_fuel_consumption())

    main_surface.blit(test_ship.texture, (test_ship.x - test_ship.texture.get_rect().centerx, test_ship.y -
                                          test_ship.texture.get_rect().centery))

    stats.update()
    main_surface.blit(stats, (0, RESOLUTION[1] - 100))

    pygame.display.update()

pygame.quit()
