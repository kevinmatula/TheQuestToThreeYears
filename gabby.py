import pygame

pygame.init()
pygame.mixer.init()


class Gabby:
    # constants
    STANDARD_VELOCITY = 5
    SHIFT_VELOCITY = 9
    JUMP_VELOCITY = 20
    VERTICAL_GRAVITY = 20
    ROLLING_VELOCITY = 11

    def __init__(self):
        # Position and state variables
        self.x = 0
        self.y = 800
        self.current_velocity = 0
        self.horizontal_velocity = self.STANDARD_VELOCITY
        self.health = 3
        self.dash_status = 5

        # Movement flags
        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.preparing_to_jump = False
        self.running = False
        self.ready_to_roll_right = False
        self.ready_to_roll_left = False
        self.line_bool = False
        self.can_overlay = False
        self.sword_attack_right = False
        self.sword_attack_left = False
        self.sword_attack = False
        self.jumped = False
        self.can_animate_jump = False
        self.invincible = False


        # Animation arrays
        self.walking_right = [
            "sprites\\gabby-sprite\\Walking\\gab_walking_right (1).png",
            "sprites\\gabby-sprite\\Walking\\gab_walking_right (2).png",
            "sprites\\gabby-sprite\\Walking\\gab_walking_right (3).png",
            "sprites\\gabby-sprite\\Walking\\gab_walking_right (4).png",
            "sprites\\gabby-sprite\\Walking\\gab_walking_right (5).png",
            "sprites\\gabby-sprite\\Walking\\gab_walking_right (6).png",
            "sprites\\gabby-sprite\\Walking\\gab_walking_right (7).png",
            "sprites\\gabby-sprite\\Walking\\gab_walking_right (8).png",
        ]
        self.walking_left = [
            "sprites\\gabby-sprite\\Walking-Left\\gab_walking_left (1).png",
            "sprites\\gabby-sprite\\Walking-Left\\gab_walking_left (2).png",
            "sprites\\gabby-sprite\\Walking-Left\\gab_walking_left (3).png",
            "sprites\\gabby-sprite\\Walking-Left\\gab_walking_left (4).png",
            "sprites\\gabby-sprite\\Walking-Left\\gab_walking_left (5).png",
            "sprites\\gabby-sprite\\Walking-Left\\gab_walking_left (6).png",
            "sprites\\gabby-sprite\\Walking-Left\\gab_walking_left (7).png",
            "sprites\\gabby-sprite\\Walking-Left\\gab_walking_left (8).png",
        ]
        self.sprinting_right = [
            "sprites\\gabby-sprite\\Running\\gab_running_right (1).png",
            "sprites\\gabby-sprite\\Running\\gab_running_right (2).png",
            "sprites\\gabby-sprite\\Running\\gab_running_right (3).png",
            "sprites\\gabby-sprite\\Running\\gab_running_right (4).png",
            "sprites\\gabby-sprite\\Running\\gab_running_right (5).png",
            "sprites\\gabby-sprite\\Running\\gab_running_right (6).png",
            "sprites\\gabby-sprite\\Running\\gab_running_right (7).png",
            "sprites\\gabby-sprite\\Running\\gab_running_right (8).png",
        ]
        self.sprinting_left = [
            "sprites\\gabby-sprite\\Running\\gab_running_left (1).png",
            "sprites\\gabby-sprite\\Running\\gab_running_left (2).png",
            "sprites\\gabby-sprite\\Running\\gab_running_left (3).png",
            "sprites\\gabby-sprite\\Running\\gab_running_left (4).png",
            "sprites\\gabby-sprite\\Running\\gab_running_left (5).png",
            "sprites\\gabby-sprite\\Running\\gab_running_left (6).png",
            "sprites\\gabby-sprite\\Running\\gab_running_left (7).png",
            "sprites\\gabby-sprite\\Running\\gab_running_left (8).png",
        ]
        self.animation_to_jump = [
            "sprites\\gabby-sprite\\Crouching\\gab_crouching (3).png",
            "sprites\\gabby-sprite\\Crouching\\gab_crouching (2).png",
            "sprites\\gabby-sprite\\Crouching\\gab_crouching (1).png",
        ]
        self.jumping = "sprites\\gabby-sprite\\Jump\\gabby_jump_up.png"
        self.prepping_jump = [
            "sprites\\gabby-sprite\\Crouching\\gab_crouching (1).png",
            "sprites\\gabby-sprite\\Crouching\\gab_crouching (2).png",
            "sprites\\gabby-sprite\\Crouching\\gab_crouching (3).png",
        ]

        self.idle_array = [
            "sprites\\gabby-sprite\\Idle\\gabby_idle (1).png",
            "sprites\\gabby-sprite\\Idle\\gabby_idle (2).png",
            "sprites\\gabby-sprite\\Idle\\gabby_idle (3).png",
            "sprites\\gabby-sprite\\Idle\\gabby_idle (4).png",
            "sprites\\gabby-sprite\\Idle\\gabby_idle (5).png",
            "sprites\\gabby-sprite\\Idle\\gabby_idle (6).png",
            "sprites\\gabby-sprite\\Idle\\gabby_idle (7).png",
            "sprites\\gabby-sprite\\Idle\\gabby_idle (8).png",
        ]

        self.rolling_right = "sprites\\gabby-sprite\\Roll\\gabby_roll (3-2).png"
        self.rolling_left = "sprites\\gabby-sprite\\Roll-Left\\gabby_roll_left (3-2).png"
        self.gabby_damage = "Sprites/gabby-sprite/gabby-damaged/spr_damage (1).png"

        self.sword_right_array = [
            "Sprites/gabby-sprite/attack-right/frame_1_attack_right_walk.png",
            "Sprites/gabby-sprite/attack-right/frame_2_attack_right_walk.png",
            "Sprites/gabby-sprite/attack-right/frame_3_attack_right_walk.png",
            "Sprites/gabby-sprite/attack-right/frame_4_attack_right_walk.png",
            "Sprites/gabby-sprite/attack-right/frame_5_attack_right_walk.png",
        ]

        self.sword_left_array = [
            "Sprites/gabby-sprite/attack-left/frame_1_attack_left_walk.png",
            "Sprites/gabby-sprite/attack-left/frame_2_attack_left_walk.png",
            "Sprites/gabby-sprite/attack-left/frame_3_attack_left_walk.png",
            "Sprites/gabby-sprite/attack-left/frame_4_attack_left_walk.png",
            "Sprites/gabby-sprite/attack-left/frame_5_attack_left_walk.png",
        ]

        # Sound effects
        self.jump_sound = pygame.mixer.Sound("Sound Effects\\Jumping\\gabby-initial-jump.wav")
        self.running_sound = pygame.mixer.Sound("Sound Effects\\Running\\running-effect-2.wav")
        self.roll_sound = pygame.mixer.Sound("Sound Effects/Rolling/rolling_sound_effect.wav")
        self.pre_roll_sound = pygame.mixer.Sound("Sound Effects/Rolling/pre_rolling_sound.wav")
        self.damage_sound = pygame.mixer.Sound("Sound Effects\\damage-gabby\\punch-noise.wav")
        #self.damage_sound = pygame.mixer.Sound("Sound Effects\\damage-gabby\\fart-funny.mp3")
        self.swing_sound = pygame.mixer.Sound("Sound Effects\\damage-gabby\\sword-swing-3.wav")

        # Frame handling for animations
        self.stop_initial_sound = 0
        self.frame_timer = 0
        self.roll_duration = 150
        self.attack_duration = 200
        self.roll_timer = 0
        self.attack_timer = 0
        self.dash_delay_timer = 1500
        self.current_frame = 0
        self.current_frame_space = 0
        self.current_frame_roll = 0
        self.frame_delay = 100
        self.attack_animation_delay = 100
        self.idle_delay = 1000
        self.idle_wait = 1000
        self.frame_timer_attack = 0
        self.current_frame_attack = 0
        self.current_gabby = pygame.image.load(self.walking_right[0])

        # gabby hitbox left
        self.gabby_rect = self.current_gabby.get_rect()
        # shrinking the rect lowkey
        self.gabby_rect.width *= 0.57
        self.gabby_rect.height *= 0.89
        self.gabby_rect.topleft = (self.x + 23, self.y + 15)
        self.gabby_rect.x = self.x + 23
        self.gabby_rect.y = self.y + 15

        self.gabby_head_rect = self.current_gabby.get_rect()
        self.gabby_head_rect.width *= 0.57
        self.gabby_head_rect.height *= 0.3
        self.gabby_head_rect.topleft = (self.x + 23, self.y + 15)
        self.gabby_head_rect.x = self.x + 23
        self.gabby_head_rect.y = self.y + 15

    # this function handles input to move gabby around
    def handle_input(self, event, screen):
        # KEYDOWN stuff
        if event.type == pygame.KEYDOWN:
            self.idle_delay = 0
            if event.key == pygame.K_d:
                self.move_right = True
            if event.key == pygame.K_a:
                self.move_left = True
            if event.key == pygame.K_LSHIFT:
                self.running = True
                self.running_sound.play(-1)
                self.horizontal_velocity = self.SHIFT_VELOCITY
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3 and (self.move_right or self.move_left) and self.dash_status == 5:
            self.can_overlay = True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.dash_status == 5:
            if self.move_left and self.sword_attack_left == False and self.sword_attack_right == False:
                self.sword_attack_left = True
                self.sword_attack_right = False
                pygame.mixer.Sound.play(self.swing_sound)
            elif self.move_right and self.sword_attack_right == False and self.sword_attack_left == False:
                self.sword_attack_right = True
                self.sword_attack_left = False
                pygame.mixer.Sound.play(self.swing_sound)

            # pygame.mixer.Sound.play(self.pre_roll_sound)
            # if there is time, you can create a whole new set of animations with green eyes, and make
            # her look cool before dashing

        # KEYUP stuff
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                self.move_right = False
            if event.key == pygame.K_a:
                self.move_left = False
            if event.key == pygame.K_LSHIFT:
                self.running = False
                self.horizontal_velocity = self.STANDARD_VELOCITY
                self.running_sound.stop()
        # this section checks for dash availability
        if event.type == pygame.MOUSEBUTTONUP and event.button == 3 and self.move_right  and self.dash_status == 5:
            self.ready_to_roll_right = True
            pygame.mixer.Sound.play(self.roll_sound)
            self.can_overlay = False

        elif event.type == pygame.MOUSEBUTTONUP and event.button == 3 and self.move_left and self.dash_status == 5:
            self.ready_to_roll_left = True
            pygame.mixer.Sound.play(self.roll_sound)
            self.can_overlay = False

    # this function updates gabbys position (if moving) and calls animate function
    def update(self, clock):
        # Update position based on movement flags
        self.dash_sword_delay(clock)
        key = pygame.key.get_pressed()
        if self.move_right:
            self.x += self.horizontal_velocity
        elif self.move_left:
            self.x -= self.horizontal_velocity
        ## updated jumping function
        if key[pygame.K_SPACE] and self.jumped == False and (not self.can_animate_jump):
            self.current_velocity = -self.VERTICAL_GRAVITY
            self.jumped = True
            self.can_animate_jump = True
            pygame.mixer.Sound.play(self.jump_sound)
            self.animate_jump(self.can_animate_jump)
        if key[pygame.K_SPACE] == False:
            self.jumped = False
        self.current_velocity += 1
        if self.current_velocity > 15:
            self.current_velocity = 15
        self.y += self.current_velocity
        ##
        if self.ready_to_roll_right:
            self.roll_right(clock)
            self.dash_delay_timer = 0
            self.dash_sword_delay(clock)
        elif self.ready_to_roll_left:
            self.roll_left(clock)
            self.dash_delay_timer = 0
            self.dash_sword_delay(clock)
        # Check if the attack is happening
        if self.sword_attack_right or self.sword_attack_left:
            self.animate_attack(self.sword_right_array if self.sword_attack_right else self.sword_left_array, clock)
            self.dash_delay_timer = 0
            self.dash_sword_delay(clock)
        else:
            if not (self.move_left or self.move_right):
                self.idle_delay += clock.get_time()
                if self.idle_delay >= self.idle_wait:
                    self.animate_movement(self.idle_array, clock)
                elif not self.can_animate_jump:
                    self.current_gabby = pygame.image.load("sprites\\gabby-sprite\\Idle\\gabby_idle (1).png")
            else:
                # Animate walking/running
                self.animate_movement(self.sprinting_right if self.running and self.move_right else
                                        self.sprinting_left if self.running and self.move_left else
                                        self.walking_right if self.move_right else
                                        self.walking_left if self.move_left else
                                        self.idle_array, clock)


            # Update hitbox position
        self.gabby_rect.topleft = (self.x + 23, self.y + 15)
        self.gabby_head_rect.topleft = (self.x + 23, self.y + 15)

    # this function does the animation!
    def animate_movement(self, animation_array, clock):
        self.frame_timer += clock.get_time()
        if self.frame_timer >= self.frame_delay:
            self.current_frame = (self.current_frame + 1) % len(animation_array)
            self.current_gabby = pygame.image.load(animation_array[self.current_frame])
            self.frame_timer = 0

    # this function animates gabby rolling right and moves her right
    def roll_right(self, clock):
        self.roll_timer += clock.get_time()
        self.invincible = True
        if self.roll_timer < self.roll_duration:
            self.current_gabby = pygame.image.load(self.rolling_right)
            self.x += self.ROLLING_VELOCITY
        else:
            self.ready_to_roll_right = False
            self.invincible = False
            self.current_frame_roll = 0  # Reset the roll frame
            self.roll_timer = 0  # Reset the roll timer

    # this function animates gabby rolling left and moves her left
    def roll_left(self, clock):
        self.roll_timer += clock.get_time()
        self.invincible = True
        if self.roll_timer < self.roll_duration:
            self.current_gabby = pygame.image.load(self.rolling_left)
            self.x -= self.ROLLING_VELOCITY
        else:
            self.ready_to_roll_left = False
            self.invincible = False
            self.current_frame_roll = 0  # Reset the roll frame
            self.roll_timer = 0  # Reset the roll timer

    def animate_jump(self, anim_jump):
        if anim_jump:
            self.current_gabby = pygame.image.load(self.jumping)

    # this function animates gabby as she prepares to jump
    def prepare_jump(self, clock):
        self.frame_timer += clock.get_time()
        if self.frame_timer >= self.frame_delay and self.current_frame_space < len(self.prepping_jump) - 1:
            self.current_frame_space = (self.current_frame_space + 1)
            self.current_gabby = pygame.image.load(self.prepping_jump[self.current_frame_space])
            self.frame_timer = 0

    def animate_attack(self, animation_array, clock):
        self.frame_timer_attack += clock.get_time()
        self.attack_timer += clock.get_time()
        if self.frame_timer_attack >= self.attack_animation_delay and self.current_frame_attack < len(animation_array) - 1:
            self.current_frame_attack = (self.current_frame_attack + 1)
            self.current_gabby = pygame.image.load(animation_array[self.current_frame_attack])
            self.frame_timer_attack = 0
        elif self.attack_timer > self.attack_duration:
            self.sword_attack_right = False
            self.sword_attack_left = False
            self.current_frame_attack = 0  # Reset the roll frame
            self.attack_timer = 0  # Reset the roll timer
        if self.sword_attack_right and self.move_left:
            self.sword_attack_right = False
            self.current_frame_attack = 0  # Reset the roll frame
            self.attack_timer = 0  # Reset the roll timer
        elif self.sword_attack_left and self.move_right:
            self.sword_attack_left = False
            self.current_frame_attack = 0  # Reset the roll frame
            self.attack_timer = 0  # Reset the roll timer

    def health_decrease(self, isHit):
        if isHit:
            self.health -= 1
            pygame.mixer.Sound.play(self.damage_sound)

    def dash_sword_delay(self, clock):
        self.dash_delay_timer += clock.get_time()
        if self.dash_delay_timer >= 1500:
            self.dash_status = 5
        elif self.dash_delay_timer >= 1200:
            self.dash_status = 4
        elif self.dash_delay_timer >= 900:
            self.dash_status = 3
        elif self.dash_delay_timer >= 600:
            self.dash_status = 2
        elif self.dash_delay_timer >= 300:
            self.dash_status = 1
        else:
            self.dash_status = 0

    def stop_movement_right(self, stopBool):
        if stopBool:
            self.move_right = False

    def stop_movement_left(self, stopBool):
        if stopBool:
            self.move_left = False

    def stop_movement_down(self, stopBool):
        if stopBool:
            self.move_up = False

    def get_current_x(self):
        return self.x

    # this function draws gabby onto the screen
    def draw(self, screen):
        screen.blit(self.current_gabby.convert_alpha(), (self.x, self.y))