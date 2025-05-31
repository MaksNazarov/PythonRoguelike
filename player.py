import pygame
from settings import PLAYER_COLOR, TILE_SIZE

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.target_x = x
        self.target_y = y
        self.rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        self.moving = False
        self.speed = 5  # pixels per frame

    def move(self, dx, dy):
        self.target_x += dx
        self.target_y += dy
        self.moving = True

    def update(self):
        if self.moving:
            dx = self.target_x * TILE_SIZE - self.rect.x
            dy = self.target_y * TILE_SIZE - self.rect.y

            # move step toward target
            if abs(dx) > 0:
                self.rect.x += self.speed if dx > 0 else -self.speed
            if abs(dy) > 0:
                self.rect.y += self.speed if dy > 0 else -self.speed

            # check if reached target
            if abs(dx) <= self.speed and abs(dy) <= self.speed:
                self.rect.x = self.target_x * TILE_SIZE
                self.rect.y = self.target_y * TILE_SIZE
                self.x = self.target_x
                self.y = self.target_y
                self.moving = False

    def draw(self, screen):
        pygame.draw.rect(screen, PLAYER_COLOR, self.rect)