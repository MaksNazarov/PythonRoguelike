import pygame
from entity.movable_entity import MovableEntity
from settings import PLAYER_COLOR, TILE_SIZE

class Player(MovableEntity):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = PLAYER_COLOR

    def draw(self, screen, tile_size=TILE_SIZE):
        rect = pygame.Rect(self.x * tile_size, self.y * tile_size, tile_size, tile_size)
        pygame.draw.rect(screen, self.color, rect)