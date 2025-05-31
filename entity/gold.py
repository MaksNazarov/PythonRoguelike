import pygame
from entity.interactable_entity import InteractableEntity
from settings import GOLD_COLOR, TILE_SIZE


class Gold(InteractableEntity):
    def __init__(self, x, y, amount=10):
        super().__init__(x, y, True)
        self.amount = amount

    def interact(self, actor):
        """
        Interaction logic when the player walks over or explicitly interacts with the gold.
        """
        print(f"{actor} picked up {self.amount} gold!")
        return True

    def draw(self, screen, tile_size=TILE_SIZE):
        rect = pygame.Rect(self.x * tile_size, self.y * tile_size, tile_size, tile_size)
        pygame.draw.rect(screen, GOLD_COLOR, rect)