import pygame
from entity.interactable.gold import Gold
from entity.interactable.level_finish import LevelFinish
from entity.movable_entity import MovableEntity
from settings import WALL_COLOR, FLOOR_COLOR, TILE_SIZE

# Map: 0 = floor, 1 = wall, 2 = gold
SMALL_MAP = [
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 2, 0, 0, 4],
    [1, 0, 0, 2, 1],
    [1, 1, 1, 1, 1],
]


BIG_MAP = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,1,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,0,1,0,1,1,1,1,1,1,0,1],
    [1,2,1,0,0,0,0,0,0,0,0,0,1,0,1],
    [1,0,1,0,1,1,1,1,1,1,1,0,1,0,1],
    [1,0,0,0,0,0,0,2,0,0,1,0,0,0,1],
    [1,1,1,1,1,1,1,0,1,1,1,1,1,0,1],
    [4,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
    [1,0,1,1,1,0,1,1,1,1,1,1,1,0,1],
    [1,0,0,0,1,0,0,2,0,0,0,0,1,0,1],
    [1,1,1,0,1,1,1,1,1,1,1,0,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,1,0,0,0,1],
    [1,0,1,1,1,1,1,1,1,0,1,1,1,0,1],
    [1,0,0,0,0,0,0,2,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    ]

class GameMap:
    def __init__(self):
        self.tile_size = TILE_SIZE
        self.map_data = BIG_MAP
        self.entities = []

        self._load_entities()


    def _load_entities(self):
        for y, row in enumerate(self.map_data):
            for x, cell in enumerate(row):
                if cell == 2: # TODO: dict/enum
                    self.entities.append(Gold(x, y))
                elif cell == 4:  # ← Level finish
                    self.entities.append(LevelFinish(x, y))


    def draw(self, screen):
        for y, row in enumerate(self.map_data):
            for x, tile in enumerate(row):
                color = WALL_COLOR if tile == 1 else FLOOR_COLOR
                rect = pygame.Rect(x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size)
                pygame.draw.rect(screen, color, rect)
        
        for entity in self.entities:
            entity.draw(screen, self.tile_size)


    def _can_be_passed(self, x, y):
        if 0 <= y < len(self.map_data) and 0 <= x < len(self.map_data[0]): # in bounds
            return self.map_data[y][x] != 1 # returns True if not a wall
        return False # out of bounds
    

    def can_be_moved(self, actor: MovableEntity, dx, dy):
        return self._can_be_passed(actor.x + dx, actor.y + dy)