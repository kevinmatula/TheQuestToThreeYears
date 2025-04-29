import pygame
from menu import Button

class RestartLevelTwo:

    def __init__(self, screen, gameStateManager):
        self.screen = screen
        self.gameStateManager = gameStateManager

    def run(self, events, elapsed_time):
        self.screen.fill((30, 30, 30))
        (mouse_pos_x, mouse_pos_y) = pygame.mouse.get_pos()

        DEATH_TEXT = pygame.font.Font("Fonts\\TitleScreen5.ttf", 60).render("Try This Level ... Again ?", True, "#FFFFFF")
        DEATH_RECT = DEATH_TEXT.get_rect(center=(960, 100))

        GABBY_GRAVE = pygame.image.load("sprites\\environment-stuff\\cat-grave.png")

        self.PLAY_BUTTON = Button(base_image=pygame.image.load("sprites\\environment-stuff\\re-do.png"),
                                  hovering_image=pygame.image.load
                                  ("sprites\\environment-stuff\\re-do-hovering.png"), x=960, y=340)

        self.screen.blit(DEATH_TEXT, DEATH_RECT)
        self.screen.blit(GABBY_GRAVE, (550, 380))

        self.PLAY_BUTTON.changeHovering(mouse_pos_x, mouse_pos_y)
        self.PLAY_BUTTON.update(self.screen)
