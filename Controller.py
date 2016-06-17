import pygame
from pygame.locals import *


class Controller:
    def __init__(self):
        self.pressed_keys = []
        self.active = True
        self.exit = False

    def update(self):
        if self.active:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key not in self.pressed_keys:
                        self.pressed_keys.append(event.key)
                if event.type == KEYUP:
                    self.pressed_keys.remove(event.key)
                elif event.type == QUIT:
                    self.exit = True
