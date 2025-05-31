import pygame
from core.game_master import GameMaster
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from entity.player import Player
from map.map import GameMap
    

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    game_map = GameMap()
    player = Player(1, 1)
    game_master = GameMaster(screen, game_map, player)

    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        game_master.handle_input(keys)
        game_master.update()
        game_master.draw()

    pygame.quit()