import random

import pygame
from entity.interactable_entity import InteractableEntity
from entity.movable_entity import MovableEntity
# from map.map import GameMap # FIXME: circular import
from settings import ENEMY_COLOR


class Enemy(MovableEntity, InteractableEntity):
    def __init__(self, x, y):
        MovableEntity.__init__(self, x, y)
        InteractableEntity.__init__(self, x, y)
        self.color = ENEMY_COLOR
        self.speed = 2

    def draw(self, screen, tile_size):
        rect = pygame.Rect(self.x * tile_size, self.y * tile_size, tile_size, tile_size)
        pygame.draw.rect(screen, self.color, rect)

    def interact(self, actor):
        # print("Player interacts with enemy – attack!")
        return True

    def update(self, game_map, player):
        """
        Basic AI: Move randomly toward the player.
        """
        if not self.moving:
            # print("Enemy tries to move!")
            dx = player.x - self.x
            dy = player.y - self.y

            move_x = 1 if dx > 0 else -1 if dx < 0 else 0
            move_y = 1 if dy > 0 else -1 if dy < 0 else 0

            # try to move horizontally first
            if abs(dx) > abs(dy):
                if game_map.can_be_moved(self, move_x, 0):
                    self.move(move_x, 0)
                elif game_map.can_be_moved(self, 0, move_y):
                    self.move(0, move_y)
            else:
                if game_map.can_be_moved(self, 0, move_y):
                    self.move(0, move_y)
                elif game_map.can_be_moved(self, move_x, 0):
                    self.move(move_x, 0)

            # print(move_x, move_y)