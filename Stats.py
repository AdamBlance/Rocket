import pygame
pygame.font.init()


class Stats(pygame.Surface):
    font = pygame.font.SysFont('arial', 18)
    colour = [255, 255, 255]

    def __init__(self, ship):
        self.ship = ship
        super(Stats, self).__init__((300, 100))

    def update(self):

        self.fill([0, 0, 0])

        vertical_velocity_text = self.font.render('Vertical velocity: %s%s' % (round(self.ship.dy, 1), 'ms⁻¹'),
                                                  False, self.colour)
        horizontal_velocity_text = self.font.render('Horizontal velocity: %s%s' % (round(self.ship.dx, 1), 'ms⁻¹'),
                                                    False, self.colour)
        throttle_text = self.font.render('Throttle: %s%s' % (round((self.ship.throttle * 100), 0), '%'),
                                         False, self.colour)
        bearing_text = self.font.render('Bearing: %s' % self.ship.bearing,
                                        False, self.colour)
        total_fuel_text = self.font.render('Total fuel: %s%s' % (round(self.ship.get_total_fuel(), 0), 'l'),
                                           False, self.colour)

        self.blit(vertical_velocity_text, (0, 0))
        self.blit(horizontal_velocity_text, (0, 20))
        self.blit(throttle_text, (0, 40))
        self.blit(bearing_text, (0, 60))
        self.blit(total_fuel_text, (0, 80))
