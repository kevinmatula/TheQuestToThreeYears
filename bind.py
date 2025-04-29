import pygame


class Button:

    def __init__(self, base_image, hovering_image, x, y):
        self.base_image = base_image
        self.hovering_image = hovering_image
        self.x_pos = x
        self.y_pos = y
        self.current_image = base_image
        self.rect = self.current_image.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        screen.blit(self.current_image, self.rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def changeHovering(self, x, y):
        if x in range(self.rect.left, self.rect.right) and y in range(self.rect.top,
                                                                                        self.rect.bottom):
            self.current_image = self.hovering_image
        else:
            self.current_image = self.base_image


class Bind:

    def __init__(self, screen, gameStateManager):
        self.screen = screen
        self.gameStateManager = gameStateManager

    def run(self, events, elapsed_time):
        self.screen.fill((247, 255, 245))
        (mouse_pos_x, mouse_pos_y) = pygame.mouse.get_pos()

        MENU_TEXT = pygame.font.Font("Fonts\\TitleScreen5.ttf", 125).render("Key Bindings", True, "#000000")
        MENU_RECT = MENU_TEXT.get_rect(center=(960, 100))

        BIND2_TEXT = pygame.font.Font("Fonts\\TitleScreen5.ttf", 80).render("Left Click to Use Your Paintbrush", True, "#000000")
        BIND2_RECT = BIND2_TEXT.get_rect(center=(960, 500))

        BIND1_TEXT = pygame.font.Font("Fonts\\TitleScreen5.ttf", 80).render("Right Click to Dash", True, "#000000")
        BIND1_RECT = BIND1_TEXT.get_rect(center=(960, 700))


        self.OUT_BUTTON = Button(base_image=pygame.image.load("sprites\\environment-stuff\\x-out.png"),
                                  hovering_image=pygame.image.load
                                  ("sprites\\environment-stuff\\x-out-hovering.png"), x=100, y=100)

        self.screen.blit(MENU_TEXT, MENU_RECT)
        self.screen.blit(BIND1_TEXT, BIND1_RECT)
        self.screen.blit(BIND2_TEXT, BIND2_RECT)

        for button in [self.OUT_BUTTON]:
            button.changeHovering(mouse_pos_x, mouse_pos_y)
            button.update(self.screen)
