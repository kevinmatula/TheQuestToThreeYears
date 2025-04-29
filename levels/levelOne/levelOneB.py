import pygame
import sys
from gabby import Gabby  # Import the Gabby class
from env import Env
from enemy import Enemy
import random
import math

BLACK = 128, 128, 128


class LevelOneB:
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

        self.blocks = [
            (self.floor_block, 0, 925), (self.floor_block, (self.mult_64 *  1), 925),
            (self.floor_block, (self.mult_64 *  1) + 100, 625), (self.floor_block, (self.mult_64 *  2) + 100, 625),
            (self.floor_block, (self.mult_64 * 3) + 100, 325), (self.floor_block, (self.mult_64 * 4) + 100, 325),
            (self.floor_block, (self.mult_64 * 14) + 100, 325), (self.floor_block, (self.mult_64 * 15) + 100, 325),
            (self.floor_block, (self.mult_64 * 24), 925), (self.floor_block, (self.mult_64 * 25), 925),
            (self.floor_block, (self.mult_64 * 26), 925), (self.floor_block, (self.mult_64 * 27), 925),
            (self.floor_block, (self.mult_64 * 28), 925), (self.floor_block, (self.mult_64 * 29), 925),
            (self.floor_block, (self.mult_64 * 30), 925)]

        self.barrier_left_blocks = [(self.floor_block, (self.mult_64 * -1), 861),
                                    (self.floor_block, (self.mult_64 * -1), 797),
                                    (self.floor_block, (self.mult_64 * -1), 733),
                                    (self.floor_block, (self.mult_64 * -1), 669)]
        self.barrier_right_blocks = [(self.floor_block, (self.mult_64 * 30), 861),
                                     (self.floor_block, (self.mult_64 * 30), 797),
                                     (self.floor_block, (self.mult_64 * 30), 733),
                                     (self.floor_block, (self.mult_64 * 30), 669)]
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

                # Check each block for collision with the enemy
                for block in self.blocks:
                    block_rect = pygame.Rect(block[1], block[2], block[0].get_width(), block[0].get_height())

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
        self.y1 += 20
        self.y += 20
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
        self.gabby.draw(self.screen)

    def setHealth(self, temp_health):
        self.gabby.health = temp_health

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
