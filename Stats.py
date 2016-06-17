import pygame
pygame.font.init()


class Stats(pygame.Surface):
    font = pygame.font.SysFont('arial', 18)
    colour = [255, 255, 255]

    def __init__(self, ship):

        self.ship = ship

        self.vertical_velocity = ship.dy
        self.horizontal_velocity = ship.dx
        self.throttle = ship.throttle
        self.bearing = ship.bearing
        self.total_fuel = ship.get_total_fuel()

        super(Stats, self).__init__((300, 120))

        vertical_velocity = self.font.render('Vertical velocity: %s%s' % (round(self.vertical_velocity, 1), 'ms⁻¹'), False, self.colour)
        horizontal_velocity = self.font.render('Horizontal velocity: %s%s' % (round(self.horizontal_velocity, 1), 'ms⁻¹'), False, self.colour)
        throttle = self.font.render('Throttle: %s%s' % (round((self.throttle * 100), 0), '%'), False, self.colour)
        bearing = self.font.render('Bearing: %s' % self.bearing, False, self.colour)
        total_fuel = self.font.render('Total fuel: %s%s' % (round(self.total_fuel, 0), 'l'), False, self.colour)

        self.blit(vertical_velocity, (0, 0))
        self.blit(horizontal_velocity, (0, 20))
        self.blit(throttle, (0, 40))
        self.blit(bearing, (0, 60))
        self.blit(total_fuel, (0, 80))

    def update(self):
        self.__init__(self.ship)
