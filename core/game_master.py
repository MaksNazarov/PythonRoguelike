import pygame

from entity.player import Player
from map.map import GameMap


class GameMaster:
    def __init__(self, screen: pygame.Surface, game_map: GameMap, player: Player):
        self.screen = screen
        self.game_map = game_map
        self.player = player
        self.tile_size = game_map.tile_size

    def handle_input(self, keys):
        if not self.player.moving:
            if keys[pygame.K_UP]:
                self.player.move(0, -1, self.game_map)
            elif keys[pygame.K_DOWN]:
                self.player.move(0, 1, self.game_map)
            elif keys[pygame.K_LEFT]:
                self.player.move(-1, 0, self.game_map)
            elif keys[pygame.K_RIGHT]:
                self.player.move(1, 0, self.game_map)

    def update(self):
        self.player.update_position(self.tile_size)

    def draw(self):
        self.game_map.draw(self.screen)
        self.player.draw(self.screen, self.tile_size)
        pygame.display.flip()