import pygame

from entity.interactable.level_finish import LevelFinish
from entity.interactable_entity import InteractableEntity
from entity.movable.player import Player
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

    def handle_interaction(self):
        for entity in self.game_map.entities:
            if isinstance(entity, InteractableEntity) and entity.x == self.player.x and entity.y == self.player.y: # TODO: clean up condition
                success = entity.interact(self.player)
                if success:
                    if isinstance(entity, LevelFinish):
                            self.advance_level()
                    if entity.remove_on_interact:
                        self.game_map.entities.remove(entity)
                break

    def update(self):
        self.player.update_position(self.tile_size)
        if not self.player.moving:
            self.handle_interaction()

    def advance_level(self):
        """Moves player over to the next level if it exists; if not, makes him win"""
        print("Advancing to the next level...")
        self.game_map = GameMap() # TODO: load new map
        self.player.x, self.player.y = 1, 1 # TODO: player position into map

    def draw(self):
        self.game_map.draw(self.screen)
        self.player.draw(self.screen, self.tile_size)
        pygame.display.flip()