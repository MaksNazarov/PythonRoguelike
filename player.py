import pygame
from settings import PLAYER_COLOR, TILE_SIZE

class Player:
    x: int
    y: int


    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)


    def move(self, dx, dy):
        self.rect.x += dx * TILE_SIZE
        self.rect.y += dy * TILE_SIZE


    def draw(self, screen):
        pygame.draw.rect(screen, PLAYER_COLOR, self.rect)