from entity.entity import Entity
from settings import TILE_SIZE

class MovableEntity(Entity):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.target_x = x
        self.target_y = y
        self.moving = False
        self.speed = 5  # pixels per frame

    def move(self, dx, dy):
        self.target_x = self.x + dx
        self.target_y = self.y + dy
        self.moving = True

    def update_position(self, tile_size=TILE_SIZE):
        if self.moving:
            dx = self.target_x * tile_size - self.x * tile_size
            dy = self.target_y * tile_size - self.y * tile_size

            # move step toward target
            if abs(dx) > 0:
                self.x += self.speed / tile_size if dx > 0 else -self.speed / tile_size
            if abs(dy) > 0:
                self.y += self.speed / tile_size if dy > 0 else -self.speed / tile_size

            # check if reached target
            if abs(dx) <= self.speed and abs(dy) <= self.speed:
                self.x = self.target_x
                self.y = self.target_y
                self.moving = False