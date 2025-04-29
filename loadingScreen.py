import pygame

class LoadingScreen:

    def __init__(self, screen, gameStateManager, clock):
        self.screen = screen
        self.clock = clock
        self.gameStateManager = gameStateManager
        self.frame_timer = 0
        self.interleave = pygame.image.load("Sprites\\environment-stuff\\Interleave.png")

    def run(self, events, elapsed_time):
        self.screen.blit(self.interleave, (0, 0))
        self.frame_timer += self.clock.get_time()
