import pygame

from entity.interactable.death_block import DeathBlock
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

            movement = (0, 0)
            if keys[pygame.K_UP]:
                movement = (0, -1)
            elif keys[pygame.K_DOWN]:
                movement = (0, 1)
            elif keys[pygame.K_LEFT]:
                movement = (-1, 0)
            elif keys[pygame.K_RIGHT]:
                movement = (1, 0)
            
            if self.game_map.can_be_moved(self.player, movement[0], movement[1]):
                self.player.move(movement[0], movement[1])

    def handle_interaction(self):
        for entity in self.game_map.entities:
            if isinstance(entity, InteractableEntity) and entity.x == self.player.x and entity.y == self.player.y: # TODO: clean up condition: not only player can interact
                success = entity.interact(self.player)
                if success:
                    if isinstance(entity, LevelFinish):
                        self.advance_level()
                    elif isinstance(entity, DeathBlock):
                        self.reset()
                    if entity.remove_on_interact:
                        self.game_map.entities.remove(entity)
                break

    def update(self):
        self.player.update_position(self.tile_size)
        if not self.player.moving:
            self.handle_interaction()

    def advance_level(self):
        """Moves player over to the next level if it exists; if not, makes him win"""
        print(f"Advancing to the level {self.player.state.level} with gold {self.player.state.gold}")
        self.game_map = GameMap() # TODO: load new map
        self.player.x, self.player.y = 1, 1 # TODO: player position into map

    def reset(self):
        """Resets player state"""
        print("You lost!")
        self.player.state.reset()
        self.game_map = GameMap() # TODO: load first map/map generator
        self.player.x, self.player.y = 1, 1

    def draw(self):
        self.game_map.draw(self.screen)
        self.player.draw(self.screen, self.tile_size)
        pygame.display.flip()