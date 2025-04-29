import pygame
import sys
from gabby import Gabby  # Import the Gabby class
from env import Env
from enemy import Enemy
import random
import math

BLACK = 128, 128, 128


class LevelOneA:
    def __init__(self, screen, gameStateManager, clock):
        # intializations of classes and clock
        self.original_x = None
        self.gabby_health = None
        self.screen = screen
        self.gameStateManager = gameStateManager
        self.clock = clock
        self.gabby = Gabby()
        self.time = 0
        BG_images = ["Sprites/environment-stuff/rainy-background.png"]
        current_image = pygame.image.load(BG_images[0])
        self.faster_surface = current_image.convert()
        self.scroll = 0

        # intializations of environment and enemy
        self.enemy1 = Enemy(self.gabby, random.randint(400, 1400), 800, random.randint(1, 3), False, (0, 0, 0))
        self.enemy2 = Enemy(self.gabby, random.randint(400, 1400), 800, random.randint(1, 3), False, (0, 0, 0))
        self.enemy3 = Enemy(self.gabby, random.randint(400, 1400), 800, random.randint(1, 3), False, (0, 0, 0))
        self.enemy4 = Enemy(self.gabby, random.randint(400, 1400), 800, random.randint(1, 3), False, (0, 0, 0))
        self.enemy5 = Enemy(self.gabby, random.randint(400, 1400), 800, random.randint(1, 3), False, (0, 0, 0))
        self.enemy6 = Enemy(self.gabby, random.randint(400, 1400), 800, random.randint(1, 3), False, (0, 0, 0))
        self.enemies = [self.enemy1, self.enemy2, self.enemy3, self.enemy4, self.enemy5, self.enemy6]
        self.cats = []
        self.env = Env()
        self.mult_64 = 64

        # cat image
        self.cat_images = [
            pygame.image.load("Sprites/environment-stuff/cat-animation/cat-2 (1).png"),
            pygame.image.load("Sprites/environment-stuff/cat-animation/cat-2 (2).png"),
            pygame.image.load("Sprites/environment-stuff/cat-animation/cat-2 (3).png"),
            pygame.image.load("Sprites/environment-stuff/cat-animation/cat-2 (4).png"),
            pygame.image.load("Sprites/environment-stuff/cat-animation/cat-2 (5).png"),
            pygame.image.load("Sprites/environment-stuff/cat-animation/cat-2 (6).png")
            ]

        self.x = 0
        self.y = 0
        self.x1 = 0
        self.y1 = -self.faster_surface.get_height()


        self.block_image = pygame.image.load("Sprites/environment-stuff/Block.png")
        self.floor_block = pygame.image.load("Sprites/environment-stuff/floor-block.png")

        self.blocks = [##the first row are the silly blocks
            (self.floor_block, (self.mult_64 *  6), 700), (self.floor_block, (self.mult_64 *  9), 400),
            (self.floor_block, (self.mult_64 * 12), 500),
            ##the following rows are the floor
            (self.floor_block, 0, 925), (self.floor_block, (self.mult_64 *  1), 925),
            (self.floor_block, (self.mult_64 *  2), 925), (self.floor_block, (self.mult_64 *  3), 925),
            (self.floor_block, (self.mult_64 *  4), 925), (self.floor_block, (self.mult_64 *  5), 925),
            (self.floor_block, (self.mult_64 *  6), 925), (self.floor_block, (self.mult_64 *  7), 925),
            (self.floor_block, (self.mult_64 *  8), 925), (self.floor_block, (self.mult_64 *  9), 925),
            (self.floor_block, (self.mult_64 *  10), 925), (self.floor_block, (self.mult_64 *  11), 925),
            (self.floor_block, (self.mult_64 * 12), 700), (self.floor_block, (self.mult_64 *  13), 700),
            (self.floor_block, (self.mult_64 *  14), 925), (self.floor_block, (self.mult_64 *  15), 925),
            (self.floor_block, (self.mult_64 *  16), 925), (self.floor_block, (self.mult_64 *  17), 925),
            (self.floor_block, (self.mult_64 *  18), 925), (self.floor_block, (self.mult_64 *  19), 925),
            (self.floor_block, (self.mult_64 *  20), 925), (self.floor_block, (self.mult_64 *  21), 925),
            (self.floor_block, (self.mult_64 *  22), 925), (self.floor_block, (self.mult_64 *  23), 925),
            (self.floor_block, (self.mult_64 *  24), 925), (self.floor_block, (self.mult_64 *  25), 925),
            (self.floor_block, (self.mult_64 *  26), 925), (self.floor_block, (self.mult_64 *  27), 925),
            (self.floor_block, (self.mult_64 *  28), 925), (self.floor_block, (self.mult_64 *  29), 925),
            (self.floor_block, (self.mult_64 *  30), 925)]

        self.barrier_left_blocks = [(self.floor_block, (self.mult_64 *  -1), 861), (self.floor_block, (self.mult_64 *  -1), 797),
                                    (self.floor_block, (self.mult_64 *  -1), 733), (self.floor_block, (self.mult_64 *  -1), 669)]
        self.barrier_right_blocks = [(self.floor_block, (self.mult_64 * 30), 861), (self.floor_block, (self.mult_64 * 30), 797),
                                     (self.floor_block, (self.mult_64 *  30), 733), (self.floor_block, (self.mult_64 *  30), 669)]
        self.block_rect = [(self.blocks[0][0].get_rect()), ]

        # Basic Sound Effects
        self.enemy_death = pygame.mixer.Sound("Sound Effects\\Death Sound Effect Enemy\\meow.wav")
        self.enemy_death_fall = pygame.mixer.Sound("Sound Effects\\Death Sound Effect Enemy\\meow.mp3")
        self.original_y = self.gabby.y

    # this is a very simple run function, and updates movement and enemy movement
    def run(self, events, elapsed_time):
        self.original_x = self.gabby.x
        self.gabby_health = self.gabby.health
        self.time = elapsed_time
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
            self.gabby.handle_input(event, self.screen)

        for enemy in self.enemies:
            enemy.update(self.clock)
            enemy.enemy_move(self.clock)
            if enemy.isRemovable:  # If True, Gabby collided with the enemy while rolling
                new_cat = [enemy.x, enemy.y + 10, 0, 0]
                self.cats.append(new_cat)
                self.enemies.remove(enemy)  # Remove the enemy from the list
                pygame.mixer.Sound.play(self.enemy_death)
            elif enemy.y > 1000:
                self.enemies.remove(enemy)  # Remove the enemy from the list
                pygame.mixer.Sound.play(self.enemy_death_fall)
        for block in self.blocks:
            block_rect = pygame.Rect(block[1], block[2], block[0].get_width(), block[0].get_height())
            block_bottom_rect = pygame.Rect(block[1], block[2] + block[0].get_height() - 10, block[0].get_width(), 10)
            if block_bottom_rect.colliderect(self.gabby.gabby_head_rect):
                self.gabby.y = block_rect.top + 50
                self.gabby.current_velocity += 2
            elif block_rect.colliderect(self.gabby.gabby_rect):
                self.gabby.y = block_rect.top - 130
                self.gabby.can_animate_jump = False
                if self.gabby.current_velocity >= 0:
                    self.gabby.current_velocity += 1

            for enemy in self.enemies:
                enemy_on_block = False  # Assume the enemy is not on a block for this frame

                # Check each block for collision with the enemy
                for block in self.blocks:
                    block_rect = pygame.Rect(block[1], block[2], block[0].get_width(), block[0].get_height())

                    if block_rect.colliderect(enemy.enemy_rect):
                        # Enemy is standing on the block, position them on top
                        enemy.y = block_rect.top - 115
                        enemy_on_block = True  # Enemy is on a block, set flag to True
                        break  # No need to check further blocks if already on one


                # If the enemy is not on any block, set them back to ground level
                if not enemy_on_block:
                    enemy.fall()



                enemy.enemy_rect.x = enemy.x + 23
                enemy.enemy_rect.y = enemy.y + 20

        for block in self.barrier_left_blocks:
            self.original_x = self.gabby.x
            block_rect = pygame.Rect(block[1], block[2], block[0].get_width(), block[0].get_height())
            if block_rect.colliderect(self.gabby.gabby_rect):
                self.gabby.move_left = False

        for block in self.barrier_right_blocks:
            self.original_x = self.gabby.x
            block_rect = pygame.Rect(block[1], block[2], block[0].get_width(), block[0].get_height())
            if block_rect.colliderect(self.gabby.gabby_rect):
                self.gabby.move_right = False


        self.gabby.gabby_head_rect.x = self.gabby.x + 23
        self.gabby.gabby_head_rect.y = self.gabby.y + 15
        self.gabby.gabby_rect.x = self.gabby.x + 23
        self.gabby.gabby_rect.y = self.gabby.y + 15
        self.gabby.update(self.clock)
        self.render()
        self.env.run(self.gabby)

    # this function draws everything for the scene, gets called every tick
    def render(self):
        self.y1 += 15
        self.y += 15
        self.screen.blit(self.faster_surface, (self.x, self.y))
        self.screen.blit(self.faster_surface, (self.x1, self.y1))
        if self.y > self.faster_surface.get_height():
            self.y = -self.faster_surface.get_height()
        if self.y1 > self.faster_surface.get_height():
            self.y1 = -self.faster_surface.get_height()
        self.env.draw(self.screen, self.gabby, self.time)
        for block in self.blocks:
            self.screen.blit(block[0].convert_alpha(), (block[1], block[2]))
        self.update_and_draw_cats()
        for enemy in self.enemies:
            enemy.draw(self.screen)
        self.gabby.draw(self.screen)

    def update_and_draw_cats(self):
        for cat in self.cats:
            x, y, frame_index, timer = cat

            # Update the animation timer
            timer += self.clock.get_time()
            if timer >= 200:  # Switch frame every 200ms
                frame_index = (frame_index + 1) % len(self.cat_images)
                timer = 0  # Reset the timer

            # Update the cat's frame and timer
            cat[2] = frame_index  # Update frame index
            cat[3] = timer  # Update timer

            # Draw the cat at the current frame
            current_cat_image = self.cat_images[frame_index]
            self.screen.blit(current_cat_image.convert_alpha(), (x, y))
