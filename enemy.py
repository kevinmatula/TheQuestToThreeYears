import pygame
import random

pygame.init()

## The enemy class deals with creating one enemy
## and the following it does to our hero
class Enemy:
    ## constants for the enemy
    JUMP_VELOCITY = 20
    VERTICAL_GRAVITY = 1
    Y_LOCATION = 800
    ENEMY_RADIUS = 900
    DASH_DISTANCE = 150

    def __init__(self, gabby, temp_x, temp_y, temp_speed, temp_bool, temp_color):
        # Position and state variables
        self.x = temp_x
        self.y = temp_y
        self.STANDARD_VELOCITY = temp_speed
        self.IDLE_VELOCITY = random.randint(1, 3)
        self.current_velocity = self.JUMP_VELOCITY
        self.horizontal_velocity = self.STANDARD_VELOCITY
        self.color = temp_color
        self.overlaying = temp_bool
        self.gabby = gabby
        self.right = False
        self.left = False
        self.attack = True

        # Movement flags
        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.preparing_to_jump = False
        self.running = False
        self.move_idle_right = False
        self.move_idle_left = False
        self.isRemovable = False
        self.stopBool_left = False
        self.stopBool_right = False
        self.general_idle = False

        ## animation arrays
        self.walking_right = [
            "sprites\\anti-gabby-sprite\\enemy-walk-right\\enemy_walking_right (1).png",
            "sprites\\anti-gabby-sprite\\enemy-walk-right\\enemy_walking_right (2).png",
            "sprites\\anti-gabby-sprite\\enemy-walk-right\\enemy_walking_right (3).png",
            "sprites\\anti-gabby-sprite\\enemy-walk-right\\enemy_walking_right (4).png",
            "sprites\\anti-gabby-sprite\\enemy-walk-right\\enemy_walking_right (5).png",
            "sprites\\anti-gabby-sprite\\enemy-walk-right\\enemy_walking_right (6).png",
            "sprites\\anti-gabby-sprite\\enemy-walk-right\\enemy_walking_right (7).png",
            "sprites\\anti-gabby-sprite\\enemy-walk-right\\enemy_walking_right (8).png"
        ]

        self.walking_left = [
            "sprites\\anti-gabby-sprite\\enemy-walk-left\\enemy_walking_left (1).png",
            "sprites\\anti-gabby-sprite\\enemy-walk-left\\enemy_walking_left (2).png",
            "sprites\\anti-gabby-sprite\\enemy-walk-left\\enemy_walking_left (3).png",
            "sprites\\anti-gabby-sprite\\enemy-walk-left\\enemy_walking_left (4).png",
            "sprites\\anti-gabby-sprite\\enemy-walk-left\\enemy_walking_left (5).png",
            "sprites\\anti-gabby-sprite\\enemy-walk-left\\enemy_walking_left (6).png",
            "sprites\\anti-gabby-sprite\\enemy-walk-left\\enemy_walking_left (7).png",
            "sprites\\anti-gabby-sprite\\enemy-walk-left\\enemy_walking_left (8).png"
        ]

        self.walking_slow_left = [
            "sprites\\anti-gabby-sprite\\walking-crouched-left\\gabby_walking_crouched_left (1).png",
            "sprites\\anti-gabby-sprite\\walking-crouched-left\\gabby_walking_crouched_left (2).png",
            "sprites\\anti-gabby-sprite\\walking-crouched-left\\gabby_walking_crouched_left (3).png",
            "sprites\\anti-gabby-sprite\\walking-crouched-left\\gabby_walking_crouched_left (4).png",
            "sprites\\anti-gabby-sprite\\walking-crouched-left\\gabby_walking_crouched_left (5).png",
            "sprites\\anti-gabby-sprite\\walking-crouched-left\\gabby_walking_crouched_left (6).png",
            "sprites\\anti-gabby-sprite\\walking-crouched-left\\gabby_walking_crouched_left (7).png",
            "sprites\\anti-gabby-sprite\\walking-crouched-left\\gabby_walking_crouched_left (8).png"
        ]

        self.walking_slow_right = [
            "sprites\\anti-gabby-sprite\\walking-crouched-right\\gabby_walking_crouched (1).png",
            "sprites\\anti-gabby-sprite\\walking-crouched-right\\gabby_walking_crouched (2).png",
            "sprites\\anti-gabby-sprite\\walking-crouched-right\\gabby_walking_crouched (3).png",
            "sprites\\anti-gabby-sprite\\walking-crouched-right\\gabby_walking_crouched (4).png",
            "sprites\\anti-gabby-sprite\\walking-crouched-right\\gabby_walking_crouched (5).png",
            "sprites\\anti-gabby-sprite\\walking-crouched-right\\gabby_walking_crouched (6).png",
            "sprites\\anti-gabby-sprite\\walking-crouched-right\\gabby_walking_crouched (7).png",
            "sprites\\anti-gabby-sprite\\walking-crouched-right\\gabby_walking_crouched (8).png",
        ]

        self.bow_right = [
            "sprites\\anti-gabby-sprite\\enemy-bow-attack\\enem_bow_atk_left (1).png",
            "sprites\\anti-gabby-sprite\\enemy-bow-attack\\enem_bow_atk_left (2).png",
            "sprites\\anti-gabby-sprite\\enemy-bow-attack\\enem_bow_atk_left (3).png",
            "sprites\\anti-gabby-sprite\\enemy-bow-attack\\enem_bow_atk_left (4).png",
            "sprites\\anti-gabby-sprite\\enemy-bow-attack\\enem_bow_atk_left (5).png",
            "sprites\\anti-gabby-sprite\\enemy-bow-attack\\enem_bow_atk_left (6).png",
            "sprites\\anti-gabby-sprite\\enemy-bow-attack\\enem_bow_atk_left (7).png",
            "sprites\\anti-gabby-sprite\\enemy-bow-attack\\enem_bow_atk_left (8).png",
            "sprites\\anti-gabby-sprite\\enemy-bow-attack\\enem_bow_atk_left (9).png"
        ]

        self.bow_left = [
            "sprites\\anti-gabby-sprite\\enemy-bow-attack\\enem_bow_atk (1).png",
            "sprites\\anti-gabby-sprite\\enemy-bow-attack\\enem_bow_atk (2).png",
            "sprites\\anti-gabby-sprite\\enemy-bow-attack\\enem_bow_atk (3).png",
            "sprites\\anti-gabby-sprite\\enemy-bow-attack\\enem_bow_atk (4).png",
            "sprites\\anti-gabby-sprite\\enemy-bow-attack\\enem_bow_atk (5).png",
            "sprites\\anti-gabby-sprite\\enemy-bow-attack\\enem_bow_atk (6).png",
            "sprites\\anti-gabby-sprite\\enemy-bow-attack\\enem_bow_atk (7).png",
            "sprites\\anti-gabby-sprite\\enemy-bow-attack\\enem_bow_atk (8).png",
            "sprites\\anti-gabby-sprite\\enemy-bow-attack\\enem_bow_atk (9).png",
        ]

        self.attack_left = [
            "sprites\\anti-gabby-sprite\\sword-attack\\enem_sword (2).png",
            "sprites\\anti-gabby-sprite\\sword-attack\\enem_sword (2).png",
            "sprites\\anti-gabby-sprite\\sword-attack\\enem_sword (3).png",
            "sprites\\anti-gabby-sprite\\sword-attack\\enem_sword (4).png",
            "sprites\\anti-gabby-sprite\\sword-attack\\enem_sword (5).png",
            "sprites\\anti-gabby-sprite\\sword-attack\\enem_sword (6).png"
        ]

        self.attack_right = [
            "sprites\\anti-gabby-sprite\\sword-attack\\enem_sword_left (2).png",
            "sprites\\anti-gabby-sprite\\sword-attack\\enem_sword_left (2).png",
            "sprites\\anti-gabby-sprite\\sword-attack\\enem_sword_left (3).png",
            "sprites\\anti-gabby-sprite\\sword-attack\\enem_sword_left (4).png",
            "sprites\\anti-gabby-sprite\\sword-attack\\enem_sword_left (5).png",
            "sprites\\anti-gabby-sprite\\sword-attack\\enem_sword_left (6).png"
        ]

        self.idle_anim = [
            "sprites\\anti-gabby-sprite\\enemy_idle\\spr_idle (1).png",
            "sprites\\anti-gabby-sprite\\enemy_idle\\spr_idle (2).png",
            "sprites\\anti-gabby-sprite\\enemy_idle\\spr_idle (3).png",
            "sprites\\anti-gabby-sprite\\enemy_idle\\spr_idle (4).png",
            "sprites\\anti-gabby-sprite\\enemy_idle\\spr_idle (5).png",
            "sprites\\anti-gabby-sprite\\enemy_idle\\spr_idle (6).png",
            "sprites\\anti-gabby-sprite\\enemy_idle\\spr_idle (7).png",
            "sprites\\anti-gabby-sprite\\enemy_idle\\spr_idle (8).png",

        ]

        # Frame handling for animations
        self.frame_timer = 0
        self.frame_timer_attack = 0
        self.current_frame_attack = 0
        self.attack_timer = 0
        self.attack_delay = 200
        self.attack_animation_delay = 25
        self.walking_idle_timer = 2000
        self.walking_timer = 4000
        self.current_frame = 0
        self.frame_delay = 100
        self.current_enemy = pygame.image.load("sprites\\anti-gabby-sprite\\walking-crouched-left\\gabby_walking_crouched_left (2).png")
        # Create a new surface
        self.colored_surface = self.current_enemy.copy()
        self.overall_colored_surface = self.current_enemy.copy()

        self.fart_sound = pygame.mixer.Sound("Sound Effects\\fart\\fart.wav")

        # enemy hitbox
        self.enemy_rect = self.current_enemy.get_rect()
        # shrinking the rect lowkey
        self.enemy_rect.width *= 0.57
        self.enemy_rect.height *= 0.89
        self.enemy_rect.topleft = (self.x + 23, self.y + 15)
        self.enemy_rect.x = self.x + 23
        self.enemy_rect.y = self.y + 15

    # this function checks to see if gabby is within range to lock on
    # if not in range then enemy idles
    def enemy_move(self, clock):
        if self.STANDARD_VELOCITY == 0:
            self.move_right = False
            self.move_left = False
            self.left = False
            self.right = False
            self.move_idle_right = False
            self.move_idle_left = False
            self.general_idle = True
        elif self.gabby.x - self.x <= self.ENEMY_RADIUS and self.gabby.x - self.x > 60:
            self.move_right = True
            self.right = True
            self.left = False
            self.move_left = False
        elif self.gabby.x - self.x >= self.ENEMY_RADIUS*-1 and self.gabby.x - self.x < -60:
            self.move_left = True
            self.right = False
            self.left = True
            self.move_right = False
        else:
            self.walking_timer += clock.get_time()
            if self.walking_timer >= self.walking_idle_timer:
                if bool(random.randint(0, 1)):
                    self.move_idle_right = True
                    self.move_idle_left = False
                else:
                    self.move_idle_left = True
                    self.move_idle_right = False
                self.walking_timer = 0
            if self.x > 1860:
                self.move_idle_left = True
                self.move_idle_right = False
        if 60 > self.gabby.x - self.x > -60:
            if self.enemy_rect.colliderect(self.gabby.gabby_rect) and not self.gabby.invincible:
                self.attack = True
                self.attack_check(clock)
                self.move_right = False
                self.move_left = False
                self.move_idle_right = False
                self.move_idle_left = False
        else:
            self.attack_timer = 0
            self.current_frame_attack = 0
            self.frame_timer_attack = 0
            self.attack = False

    # this function moves the enemy according to gabbys position
    def update(self, clock):
        self.gabby.can_overlay
        if self.general_idle:
            self.animate_movement(self.idle_anim, clock)
        if self.attack:
            if self.right:
                self.animate_attack(self.attack_left, clock)
            else:
                self.animate_attack(self.attack_right, clock)
        if self.move_right:
            self.x += self.horizontal_velocity
            self.animate_movement(self.walking_right, clock)
        elif self.move_left:
            self.x -= self.horizontal_velocity
            self.animate_movement(self.walking_left, clock)
        elif self.move_idle_right:
            self.x += self.IDLE_VELOCITY
            self.animate_movement(self.walking_slow_right, clock)
        elif self.move_idle_left:
            self.x -= self.IDLE_VELOCITY
            self.animate_movement(self.walking_slow_left, clock)
        # this if statement checks if enemy is close enough to gabby
        # to be highlighted in red
        if self.gabby.can_overlay and abs(self.gabby.x - self.x) < self.DASH_DISTANCE and abs(self.gabby.y - self.y) < 50:
            self.colored_surface = self.current_enemy.copy()  # Copy the latest frame
            self.colored_surface.fill((222, 49, 99), special_flags=pygame.BLEND_RGB_MULT)  # Apply the red color
        else:
            self.colored_surface = self.current_enemy
        self.overall_colored_surface = self.current_enemy.copy()  # Copy the latest frame
        self.overall_colored_surface.fill(self.color, special_flags=pygame.BLEND_RGB_MULT)
        self.enemy_rect.topleft = (self.x + 23, self.y + 15)
        # decided to take this out so game can be more balanced
        #if (self.gabby.ready_to_roll_right or self.gabby.ready_to_roll_left) and self.enemy_rect.colliderect(self.gabby.gabby_rect):
         #   self.isRemovable = True
        if (self.gabby.sword_attack_right or self.gabby.sword_attack_left) and self.enemy_rect.colliderect(self.gabby.gabby_rect):
            self.isRemovable = True

    # this function animates the movement
    def animate_movement(self, animation_array, clock):
        self.frame_timer += clock.get_time()
        if self.frame_timer >= self.frame_delay:
            self.current_frame = (self.current_frame + 1) % len(animation_array)
            self.current_enemy = pygame.image.load(animation_array[self.current_frame])
            self.frame_timer = 0

    def animate_attack(self, animation_array, clock):
        self.frame_timer_attack += clock.get_time()
        if self.frame_timer_attack >= self.attack_animation_delay:
            self.current_frame_attack = (self.current_frame_attack + 1) % len(animation_array)
            self.current_enemy = pygame.image.load(animation_array[self.current_frame_attack])
            self.frame_timer_attack = 0

    def attack_check(self, clock):
        if self.attack_timer >= self.attack_delay:
            self.gabby.health_decrease(True)
            self.attack_timer = 0
        else:
            self.gabby.health_decrease(False)
        self.attack_timer += clock.get_time()

    def fall(self):
        self.y += 0.5

    # this function does the drawing
    def draw(self, screen):
        if self.gabby.can_overlay:
            screen.blit(self.colored_surface.convert_alpha(), (self.x, self.y))
        elif self.overlaying:
            screen.blit(self.overall_colored_surface.convert_alpha(), (self.x, self.y))
        else:
            screen.blit(self.current_enemy.convert_alpha(), (self.x, self.y))