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


class Gab:

    def __init__(self, screen, gameStateManager):
        self.screen = screen
        self.gameStateManager = gameStateManager

    def run(self, events, elapsed_time):
        self.screen.fill((247, 255, 245))
        (mouse_pos_x, mouse_pos_y) = pygame.mouse.get_pos()

        MENU_TEXT = pygame.font.Font("Fonts\\TitleScreen5.ttf", 125).render("Gab,", True, "#000000")
        MENU_RECT = MENU_TEXT.get_rect(center=(960, 100))

        LETTER_TEXT = pygame.font.Font("Fonts\\TitleScreen5.ttf", 20).render("For half of my life I have been in love with you. So, on this three year anniversary, I took a long time deciding what I wanted to give to you.", True, "#000000")
        LETTER_RECT = LETTER_TEXT.get_rect(center=(960, 400))
        LETTER1_TEXT = pygame.font.Font("Fonts\\TitleScreen5.ttf", 20).render("I could have given you another necklace, another ring, another cute little gift, but this time, I wanted to give you everything.", True, "#000000")
        LETTER1_RECT = LETTER1_TEXT.get_rect(center=(960, 440))
        LETTER2_TEXT = pygame.font.Font("Fonts\\TitleScreen5.ttf", 18).render("Since I started coding around the same time we started dating, I knew that this game, being a summation of years worth of learning, would be the perfect thing to give you.", True, "#000000")
        LETTER2_RECT = LETTER2_TEXT.get_rect(center=(960, 480))
        LETTER3_TEXT = pygame.font.Font("Fonts\\TitleScreen5.ttf", 12).render("At first, I struggled a lot conceptually, and I know you will definitely see the imperfection within the gameplay, but it was truly a journey. I came up with this idea in August, and have probably worked on it for around ten hours a week since then.", True, "#000000")
        LETTER3_RECT = LETTER3_TEXT.get_rect(center=(960, 520))
        LETTER4_TEXT = pygame.font.Font("Fonts\\TitleScreen5.ttf", 15).render("I know it doesn’t look like much, but creating the art, compiling the music, designing the levels, figuring out the physics, coding the damn thing, and coming up with adequate details have taken me a long,", True, "#000000")
        LETTER4_RECT = LETTER4_TEXT.get_rect(center=(960, 560))
        LETTER5_TEXT = pygame.font.Font("Fonts\\TitleScreen5.ttf", 12).render("long time (For reference, this is around 2000+ lines of code, there are around 50 different frames of animation, and there are around 30 different sound effects). I truly put my heart into this game, even sleeping through class because of it LOL.", True, "#000000")
        LETTER5_RECT = LETTER5_TEXT.get_rect(center=(960, 600))
        LETTER6_TEXT = pygame.font.Font("Fonts\\TitleScreen5.ttf", 15).render("Finally, I just want you to love and appreciate this game for what it is. I know it is definitely not perfect, but whenever you are feeling uncertain or hurt by me, all I ask is that you load up this game,", True, "#000000")
        LETTER6_RECT = LETTER6_TEXT.get_rect(center=(960, 640))
        LETTER7_TEXT = pygame.font.Font("Fonts\\TitleScreen5.ttf", 15).render("and you will truly be able to visualize the love I have for you: My special little lady, so perfect and so cute. You are truly my everything gab, and I hope you love this game.", True, "#000000")
        LETTER7_RECT = LETTER7_TEXT.get_rect(center=(960, 680))
        LETTER8_TEXT = pygame.font.Font("Fonts\\TitleScreen5.ttf", 20).render("P.S. This isn't the end of the gabby game saga, expect updates periodically <3",True, "#000000")
        LETTER8_RECT = LETTER8_TEXT.get_rect(center=(960, 740))






        self.OUT_BUTTON = Button(base_image=pygame.image.load("sprites\\environment-stuff\\x-out.png"),
                                  hovering_image=pygame.image.load
                                  ("sprites\\environment-stuff\\x-out-hovering.png"), x=100, y=100)

        self.screen.blit(MENU_TEXT, MENU_RECT)
        self.screen.blit(LETTER_TEXT, LETTER_RECT)
        self.screen.blit(LETTER1_TEXT, LETTER1_RECT)
        self.screen.blit(LETTER2_TEXT, LETTER2_RECT)
        self.screen.blit(LETTER3_TEXT, LETTER3_RECT)
        self.screen.blit(LETTER4_TEXT, LETTER4_RECT)
        self.screen.blit(LETTER5_TEXT, LETTER5_RECT)
        self.screen.blit(LETTER6_TEXT, LETTER6_RECT)
        self.screen.blit(LETTER7_TEXT, LETTER7_RECT)
        self.screen.blit(LETTER8_TEXT, LETTER8_RECT)

        for button in [self.OUT_BUTTON]:
            button.changeHovering(mouse_pos_x, mouse_pos_y)
            button.update(self.screen)
