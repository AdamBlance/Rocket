import random
import math
import pygame


class ExhaustParticle:
    all_types = []
    all_particles = []

    # Pre-rendering of particles to improve frame rate
    particle_1 = pygame.Surface((20, 20))
    pygame.draw.circle(particle_1, [255, 128, 0], (10, 10), 10)
    particle_1.set_colorkey([0, 0, 0])
    all_types.append(particle_1)
    particle_2 = pygame.Surface((20, 20))
    pygame.draw.circle(particle_2, [255, 89, 0], (10, 10), 10)
    particle_2.set_colorkey([0, 0, 0])
    all_types.append(particle_2)
    particle_3 = pygame.Surface((20, 20))
    pygame.draw.circle(particle_3, [255, 187, 0], (10, 10), 10)
    particle_3.set_colorkey([0, 0, 0])
    all_types.append(particle_3)
    particle_4 = pygame.Surface((30, 30))
    pygame.draw.circle(particle_4, [255, 128, 0], (15, 15), 15)
    particle_4.set_colorkey([0, 0, 0])
    all_types.append(particle_4)
    particle_5 = pygame.Surface((30, 30))
    pygame.draw.circle(particle_5, [255, 89, 0], (15, 15), 15)
    particle_5.set_colorkey([0, 0, 0])
    all_types.append(particle_5)
    particle_6 = pygame.Surface((30, 30))
    pygame.draw.circle(particle_6, [255, 187, 0], (15, 15), 15)
    particle_6.set_colorkey([0, 0, 0])
    all_types.append(particle_6)
    particle_7 = pygame.Surface((40, 40))
    pygame.draw.circle(particle_7, [255, 128, 0], (20, 20), 20)
    particle_7.set_colorkey([0, 0, 0])
    all_types.append(particle_7)
    particle_8 = pygame.Surface((40, 40))
    pygame.draw.circle(particle_8, [255, 89, 0], (20, 20), 20)
    particle_8.set_colorkey([0, 0, 0])
    all_types.append(particle_8)
    particle_9 = pygame.Surface((40, 40))
    pygame.draw.circle(particle_9, [255, 187, 0], (20, 20), 20)
    particle_9.set_colorkey([0, 0, 0])
    all_types.append(particle_9)

    def __init__(self, x, y, bearing, throttle, ship_dx, ship_dy):
        k = 50  # Speed constant for exhaust particles
        self.bearing = bearing
        self.dx = k * throttle * math.sin(math.radians(bearing)) + random.randint(-1, 1) * random.random() + ship_dx
        self.dy = k * throttle * math.cos(math.radians(bearing)) + random.randint(-1, 1) * random.random() - ship_dy
        self.x = x
        self.y = y
        self.texture = self.all_types[random.randint(0, 8)]

        self.all_particles.append(self)

        if len(self.all_particles) > 100:
            self.all_particles.remove(self.all_particles[0])

    def move(self):
        self.x -= self.dx
        self.y += self.dy
