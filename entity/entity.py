import pygame

class Entity:
    # TODO: size param
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen, tile_size):
        raise NotImplementedError("Subclasses must implement draw()")

    def get_rect(self, tile_size):
        return pygame.Rect(self.x * tile_size, self.y * tile_size, tile_size, tile_size)