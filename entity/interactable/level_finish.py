import pygame
from entity.interactable_entity import InteractableEntity
from settings import LEVEL_FINISH_COLOR, TILE_SIZE


class LevelFinish(InteractableEntity):
    def __init__(self, x, y):
        super().__init__(x, y)

    def draw(self, screen, tile_size=TILE_SIZE): # TODO: remove tile_size from anywhere?
        rect = pygame.Rect(self.x * tile_size, self.y * tile_size, tile_size, tile_size)
        pygame.draw.rect(screen, LEVEL_FINISH_COLOR, rect)

    def interact(self, actor): # TODO: player check?
        return True