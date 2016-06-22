from constants import *
from ExhaustParticle import ExhaustParticle
from Engine import Engine
from FuelTank import FuelTank
from Controller import Controller
from Ship import Ship
from Stats import Stats

import pygame
from pygame.locals import *

main_surface = pygame.display.set_mode(RESOLUTION)

test_fuel_tank_1 = FuelTank('small_tank')
test_fuel_tank_2 = FuelTank('medium_tank')
test_engine = Engine('basic_engine')
test_ship = Ship([test_fuel_tank_1,
                  test_fuel_tank_1,
                  test_fuel_tank_2,
                  test_engine])

keyboard = Controller()
stats = Stats(test_ship)

clock = pygame.time.Clock()
running = True
while running:

    clock.tick(MAX_FPS)
    keyboard.update()

    main_surface.fill([255, 255, 255])

    if keyboard.exit:
        running = False
    if K_LSHIFT in keyboard.pressed_keys:
        test_ship.change_throttle_by(1/90)
    if K_LCTRL in keyboard.pressed_keys:
        test_ship.change_throttle_by(-1/90)
    if K_x in keyboard.pressed_keys:
        test_ship.set_throttle_to(0)
    if K_z in keyboard.pressed_keys:
        test_ship.set_throttle_to(1)
    if K_s in keyboard.pressed_keys:
        test_ship.change_bearing_by(1)
    if K_a in keyboard.pressed_keys:
        test_ship.change_bearing_by(-1)

    if test_ship.throttle > 0:
        test_ship.create_exhaust()
    for particle in ExhaustParticle.all_particles:
        particle.move()
        main_surface.blit(particle.texture, (particle.x, particle.y))

    test_ship.move()
    test_ship.use_fuel()
    stats.update()

    # test_ship.texture has to blitted because of complications with objects.
    main_surface.blit(test_ship.texture, (test_ship.get_centre_x(), test_ship.get_centre_y()))
    main_surface.blit(stats, (0, RESOLUTION[1] - stats.get_rect().height))

    pygame.display.update()

pygame.quit()
