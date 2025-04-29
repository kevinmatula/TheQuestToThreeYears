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


class Menu:

    def __init__(self, screen, gameStateManager):
        self.screen = screen
        self.gameStateManager = gameStateManager

    def run(self, events, elapsed_time):
        self.screen.fill((247, 255, 245))
        (mouse_pos_x, mouse_pos_y) = pygame.mouse.get_pos()

        MENU_TEXT = pygame.font.Font("Fonts\\TitleScreen5.ttf", 125).render("The Quest to Three Years", True, "#000000")
        MENU_RECT = MENU_TEXT.get_rect(center=(960, 100))

        self.PLAY_BUTTON = Button(base_image=pygame.image.load("sprites\\environment-stuff\\play_button.png"),
                                  hovering_image=pygame.image.load
                                  ("sprites\\environment-stuff\\play_button_hovering.png"), x=960, y=400)
        self.OPTIONS_BUTTON = Button(base_image=pygame.image.load("sprites\\environment-stuff\\bind_button.png"),
                                  hovering_image=pygame.image.load(
                                      "sprites\\environment-stuff\\bind_button_hovering.png"), x=960, y=610)
        self.GAB_BUTTON = Button(base_image=pygame.image.load("sprites\\environment-stuff\\gab_button.png"),
                                     hovering_image=pygame.image.load(
                                         "sprites\\environment-stuff\\gab_button_hovering.png"), x=960, y=820)

        self.screen.blit(MENU_TEXT, MENU_RECT)

        for button in [self.PLAY_BUTTON, self.OPTIONS_BUTTON, self.GAB_BUTTON]:
            button.changeHovering(mouse_pos_x, mouse_pos_y)
            button.update(self.screen)
