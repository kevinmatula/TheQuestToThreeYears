import pygame


class Env:

    def __init__(self):
        self.healthX = 5
        self.healthY = 0
        self.barX = 350
        self.barY = 30
        self.gabby_health_env = None
        self.one_heart_image = pygame.image.load("sprites\\environment-stuff\\one heart.png")
        self.two_heart_image = pygame.image.load("sprites\\environment-stuff\\two hearts.png")
        self.no_health_image = pygame.image.load("sprites\\environment-stuff\\zero_health.png")
        self.health_image = pygame.image.load("sprites\\environment-stuff\\full_health.png")

        # Timer-related variables
        self.clock = pygame.time.Clock()
        self.start_time = pygame.time.get_ticks()  # Store the time when the game starts
        self.font = pygame.font.Font("Fonts\\dogicapixelbold.ttf", 22)  # Font for displaying the timer
        self.timer_color = (255, 255, 255)  # White color for the timer text

        self.bar_array = [
            "Sprites\\environment-stuff\\dash-sword-bar\\full-5.png",
            "Sprites\\environment-stuff\\dash-sword-bar\\full-4.png",
            "Sprites\\environment-stuff\\dash-sword-bar\\full-3.png",
            "Sprites\\environment-stuff\\dash-sword-bar\\full-2.png",
            "Sprites\\environment-stuff\\dash-sword-bar\\full-1.png",
            "Sprites\\environment-stuff\\dash-sword-bar\\full.png"

        ]

    def run(self, gabby):
        if gabby.y > 1080:
            gabby.health = 0

    def get_gab_health(self, gabby):
        self.gabby_health_env = gabby.health

    def draw(self, screen, gabby, elapsed_time):
        gabby.health
        gabby.dash_status
        if gabby.health == 3:
            screen.blit(self.health_image.convert_alpha(), (self.healthX, self.healthY))
        elif gabby.health == 2:
            screen.blit(self.two_heart_image.convert_alpha(), (self.healthX, self.healthY))
        elif gabby.health == 1:
            screen.blit(self.one_heart_image.convert_alpha(), (self.healthX, self.healthY))
        else:
            screen.blit(self.no_health_image.convert_alpha(), (self.healthX, self.healthY))
        screen.blit(pygame.image.load(self.bar_array[gabby.dash_status]).convert_alpha(), (self.barX, self.barY))

        # Convert to minutes, seconds, and milliseconds
        minutes = elapsed_time // 60000
        seconds = (elapsed_time % 60000) // 1000
        milliseconds = (elapsed_time % 1000)

        # Format the timer text
        timer_text = f"{minutes:02}:{seconds:02}:{milliseconds:03}"

        # Render the text
        timer_surface = self.font.render(timer_text, True, self.timer_color)
        screen.blit(timer_surface, (1700, 25))  # Display at the top-left corner
