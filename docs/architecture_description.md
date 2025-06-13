# The GAME

You lost.

## 1. Introduction

The GAME is a 2d roguelike game implemented via Python's PyGame library. The goal of the game is to pass through several procedurally generated levels, avoiding or killing monsters, and beat 3 bosses. Each time the player dies, they lose the progress achieved.

## 2. Architecture drivers
Functional requirements (following features should be fully implemented/supported):
* Procedural map generation.
* Loss of player progress on death
* Inventory, damage system, using abilities.
* Enemy NPCs who can kill the player.
* Rendered  in GUI (PyGame window).

Non-functional requirements:
* Extensibility (support for modifications).
* Performance (the map and AI are updated quickly).
* Cross-platform (can be run on systems with Python 3.10 + pip installed, Windows&Linux support).


## 3. Use cases

Following roles are considered during the development:
* Player: installs and runs the game without modifications to the files.
* Developer/modification author:  extends the game functionality, adds new NPCs/features/
* NPCs: Targets player and tries to kill him. (TODO: remove?)

## 4. User description, target audience

The project caters to old-school games fans, e.g. Pacman players, while trying to catch a fresher hipster auditory with newer roguelike design.

## 5. Component diagram
![Component Diagram](docs/component_diagram.jpg)
## 6. Class diagram
![Component Diagram](docs/class_diagram.jpg)
## 7. Interactions and states ()
![Component Diagram](docs/state_diagram.jpg)
## 8. Data description

Map data: sizes and colors, objects (gold, death blocks) points and their placement (coords).
Movable entities (player and NPCs): coords, statuses, ?(abilities availability flags).

## 9. Pattern description
1. Builder: map creation step-by-step
2. Factory: enemy creation during map building/level loading.
3. Template pattern/OOP (Base classes pointed out)
4. State pattern (Game’s behavior depends on state) 
5. Singleton (maybe?) for GameMaster and PlayerState

## 10. Project acceptance criteria

Following criteria must be met for the project to be considered finished:
1. The game runs without errors during startup, level completion, finish and exit in all testing scenarios.
2. Level generation works correctly: 
    * Each level can be technically completed.
    * Moreso, by a casual player.
    * Both the player, items and enemies are spawned into otherwise empty fields.
3. Movement: player and enemies:
    * Can move in expected situations, e.g. to empty fields.
    * Can not move in expected situations, e.g. into a block or into a field where another enemy resides.
4. Combat:
    * The player can damage enemies via use of abilities, items or in other correct game situations.
    * The player can be damaged by enemies on contact or via use of abilities.
    * Both the player and enemies die when their health is lowered to zero.
5. Interface: all interface windows appear correctly, including game menus, level visuals, player and enemy sprites, items and inventory.
6. Performance: the game runs without stutters on a PC with 4 GB RAM & 4-core processor in no less than 60 fps at all times.
### Testing scenarios:
1. Functional testing: no less than 50% of project methods/functions are covered by unit tests.
2. Integration testing
3. Stress testing: running the game in Virtual Machine with RAM, processor cores and VRAM allocated to lowest requirements mentioned above.
### Testing responsibility:
* Functional, stress testing: developers.
* Beta-testing, integration testing: outsource (developer’s younger brother is going to play this).
