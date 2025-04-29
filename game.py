import pygame
import sys
from menu import Menu
from bind import Bind
from letter import Gab
from levels.levelOne.levelOneA import LevelOneA
from levels.levelOne.levelOneB import LevelOneB
from levels.levelOne.levelOneC import LevelOneC
from levels.levelOne.levelOneD import LevelOneD
from levels.levelTwo.LevelTwoa import LevelTwoA
from levels.levelTwo.LevelTwob import LevelTwoB
from levels.levelTwo.LevelTwoc import LevelTwoC
from levels.levelTwo.levelTwod import LevelTwoD
from loadingScreen import LoadingScreen
from restartlev1a import RestartLevelOne
from restartlev2a import RestartLevelTwo
from gabby import Gabby
from cutscene1 import Cutscene
from cutscene2 import Cutscene2
from cutscene3 import Cutscene3
from cutscene4 import Cutscene4

SIZE = WIDTH, HEIGHT = 1920, 1080


# Game state manager stuff
class GameStateManager:
    def __init__(self, currentState):
        self.currentState = currentState
    def get_state(self):
        return self.currentState
    def set_state(self, state):
        self.currentState = state


# class to create game
class Game:
    def __init__(self):
        # initializations
        pygame.init()
        self.screen = pygame.display.set_mode(SIZE)
        self.clock = pygame.time.Clock()
        self.start_time = pygame.time.get_ticks()  # Start timer at game initialization
        self.gameStateManager = GameStateManager('loadingscreen')
        self.title_screen_music = pygame.mixer.Sound("Sound Effects\\Music\\Title-screen-music.wav")
        self.array_music = [
            pygame.mixer.Sound("Sound Effects\\Music\\better-title-screen-music.wav"),
            pygame.mixer.Sound("Sound Effects\\Music\\death-song.mp3"),
            pygame.mixer.Sound("Sound Effects\\Music\\death-song-2.mp3"),
            pygame.mixer.Sound("Sound Effects\\Music\\8bit-music-for-game-68698.mp3"),
            pygame.mixer.Sound("Sound Effects\\Music\\game-music-loop-7-145285.mp3")
        ]
        self.current_song_index = 0
        self.music_channel = pygame.mixer.Channel(0)  # Reserve a channel for music playback
        self.rain_sound = pygame.mixer.Sound("Sound Effects\\background-noise\\rain.wav")
        self.thunder_sound = pygame.mixer.Sound("Sound Effects\\interesting ass noises\\thunder.mp3")
        self.death_song = pygame.mixer.Sound("Sound Effects\\Music\\death-music.mp3")
        self.inquisitive_sound = pygame.mixer.Sound("Sound Effects\\interesting ass noises\\discovery.wav")
        self.title_screen_music.play(-1)
        self.menu = Menu(self.screen, self.gameStateManager)
        self.restartlev1a = RestartLevelOne(self.screen, self.gameStateManager)
        self.restartlev2a = RestartLevelTwo(self.screen, self.gameStateManager)
        self.levelonea = LevelOneA(self.screen, self.gameStateManager, self.clock)
        self.gabby = Gabby()
        self.leveloneb = LevelOneB(self.screen, self.gameStateManager, self.clock)
        self.levelonec = LevelOneC(self.screen, self.gameStateManager, self.clock)
        self.leveloned = LevelOneD(self.screen, self.gameStateManager, self.clock)
        self.leveltwoa = LevelTwoA(self.screen, self.gameStateManager, self.clock)
        self.leveltwob = LevelTwoB(self.screen, self.gameStateManager, self.clock)
        self.leveltwoc = LevelTwoC(self.screen, self.gameStateManager, self.clock)
        self.leveltwod = LevelTwoD(self.screen, self.gameStateManager, self.clock)
        self.loadingscreen = LoadingScreen(self.screen, self.gameStateManager, self.clock)
        self.cutscene1 = Cutscene(self.screen)
        self.cutscene2 = Cutscene2(self.screen)
        self.cutscene3 = Cutscene3(self.screen)
        self.cutscene4 = Cutscene4(self.screen)
        self.bind = Bind(self.screen, self.gameStateManager)
        self.gab = Gab(self.screen, self.gameStateManager)

        self.states = {'loadingscreen': self.loadingscreen,'menu': self.menu,
                       'levelonea': self.levelonea,
                       'restartlev1a' : self.restartlev1a,
                       'leveloneb' : self.leveloneb,
                       'levelonec' : self.levelonec,
                       'leveloned' : self.leveloned,
                       'cutscene1' : self.cutscene1,
                       'cutscene2' : self.cutscene2,
                       'leveltwoa' : self.leveltwoa,
                       'leveltwob' : self.leveltwob,
                       'leveltwoc': self.leveltwoc,
                       'leveltwod' : self.leveltwod,
                       'restartlev2a' : self.restartlev2a,
                       'cutscene3' : self.cutscene3,
                       'cutscene4' : self.cutscene4,
                       'bind' : self.bind,
                       'gab' : self.gab}
        self.radioPlaying = False
    def get_elapsed_time(self):
        """Calculate the elapsed time since the game started."""
        return pygame.time.get_ticks() - self.start_time

    def run(self):
        while True:
            elapsed_time = self.get_elapsed_time()
            self.clock.tick(60)
            events = pygame.event.get()
            current_state = self.gameStateManager.get_state()
            x = self.levelonea.original_x
            if current_state == 'loadingscreen' and self.loadingscreen.frame_timer >= 6000:
                self.gameStateManager.set_state('menu')

            for event in events:
                if event.type == pygame.QUIT:
                    sys.exit()
                # this section changes the level
                if current_state == 'menu':
                    if event.type == pygame.MOUSEBUTTONUP and self.menu.PLAY_BUTTON.checkForInput(pygame.mouse.get_pos()):
                        # Switch from menu to levelonea if a key is pressed
                        self.title_screen_music.fadeout(500)
                        self.gameStateManager.set_state('cutscene1') ## adjust this to dev, switch to levelonea when done
                        self.cutscene1.start() ## FOR DEV
                    elif event.type == pygame.MOUSEBUTTONUP and self.menu.OPTIONS_BUTTON.checkForInput(pygame.mouse.get_pos()):
                        # Switch from menu to levelonea if a key is pressed
                        self.gameStateManager.set_state('bind') ## adjust this to dev, switch to levelonea when done
                        # self.cutscene1.start() ## FOR DEV
                    elif event.type == pygame.MOUSEBUTTONUP and self.menu.GAB_BUTTON.checkForInput(pygame.mouse.get_pos()):
                        # Switch from menu to levelonea if a key is pressed
                        self.gameStateManager.set_state('gab') ## adjust this to dev, switch to levelonea when done
                        # self.cutscene1.start() ## FOR DEV
                if current_state == 'bind':
                    if event.type == pygame.MOUSEBUTTONUP and self.bind.OUT_BUTTON.checkForInput(pygame.mouse.get_pos()):
                        # Switch from menu to levelonea if a key is pressed
                        self.gameStateManager.set_state('menu') ## adjust this to dev, switch to levelonea when done
                        # self.cutscene1.start() ## FOR DEV
                if current_state == 'gab':
                    if event.type == pygame.MOUSEBUTTONUP and self.gab.OUT_BUTTON.checkForInput(pygame.mouse.get_pos()):
                        # Switch from menu to levelonea if a key is pressed
                        self.gameStateManager.set_state('menu') ## adjust this to dev, switch to levelonea when done
                        # self.cutscene1.start() ## FOR DEV
                if current_state == 'restartlev1a':
                    if event.type == pygame.MOUSEBUTTONUP and self.restartlev1a.PLAY_BUTTON.checkForInput(pygame.mouse.get_pos()):
                        # Switch from menu to levelonea if a key is pressed
                        self.gameStateManager.set_state('levelonea')
                        self.death_song.fadeout(1000)
                        self.rain_sound.play(-1)
                if current_state == 'restartlev2a':
                    if event.type == pygame.MOUSEBUTTONUP and self.restartlev2a.PLAY_BUTTON.checkForInput(pygame.mouse.get_pos()):
                        # Switch from menu to levelonea if a key is pressed
                        self.gameStateManager.set_state('leveltwoa')
                        self.death_song.fadeout(1000)
                        self.array_music[0].play(-1)
            if current_state == 'cutscene4':
                self.cutscene4.run(events, elapsed_time)
                if not self.cutscene4.playing:
                    pygame.quit()
            if current_state == 'cutscene2':
                self.cutscene2.run(events, elapsed_time)
                if not self.cutscene2.playing:
                    self.gameStateManager.set_state('leveltwoa') # Transition to levelonea
                    self.array_music[0].play(-1)
            elif current_state == 'cutscene3':
                self.cutscene3.run(events, elapsed_time)
                if not self.cutscene3.playing:
                    self.gameStateManager.set_state('leveltwod') # Transition to levelonea
                    self.leveltwod.setHealth(health)
                    self.array_music[3].play(-1)
            elif current_state == 'cutscene1':
                self.cutscene1.run(events, elapsed_time)
                if not self.cutscene1.playing:
                    self.start_time = pygame.time.get_ticks()
                    self.gameStateManager.set_state('levelonea')  # Transition to levelonea
                    self.rain_sound.play(-1)
            elif current_state == 'levelonea':
                health = self.levelonea.gabby_health
                if health <= 0:
                    self.levelonea.__init__(self.screen, self.gameStateManager, self.clock)
                    pygame.mixer.stop()
                    self.death_song.play(-1)
                    self.gameStateManager.set_state('restartlev1a')
                elif len(self.levelonea.enemies) == 0 and x > 1800:
                    self.levelonea.__init__(self.screen, self.gameStateManager, self.clock)
                    pygame.mixer.stop()
                    self.rain_sound.play(-1)
                    self.gameStateManager.set_state('leveloneb')
                    self.leveloneb.setHealth(health)
            elif current_state == 'leveloneb':
                x = self.leveloneb.original_x
                health = self.leveloneb.gabby_health
                if health <= 0:
                    self.leveloneb.__init__(self.screen, self.gameStateManager, self.clock)
                    pygame.mixer.stop()
                    self.death_song.play(-1)
                    self.gameStateManager.set_state('restartlev1a')
                elif x > 1800:
                    self.leveloneb.__init__(self.screen, self.gameStateManager, self.clock)
                    pygame.mixer.stop()
                    self.rain_sound.play(-1)
                    self.gameStateManager.set_state('levelonec')
                    self.levelonec.setHealth(health)
            elif current_state == 'levelonec':
                x = self.levelonec.original_x
                health = self.levelonec.gabby_health
                if health <= 0:
                    self.levelonec.__init__(self.screen, self.gameStateManager, self.clock)
                    pygame.mixer.stop()
                    self.death_song.play(-1)
                    self.gameStateManager.set_state('restartlev1a')
                elif len(self.levelonec.enemies) == 0 and x > 1800:
                    self.levelonec.__init__(self.screen, self.gameStateManager, self.clock)
                    pygame.mixer.stop()
                    self.rain_sound.play(-1)
                    self.thunder_sound.play(-1)
                    self.gameStateManager.set_state('leveloned')
                    self.leveloned.setHealth(health)
            elif current_state == 'leveloned':
                x = self.leveloned.original_x
                health = self.leveloned.gabby_health
                if health <= 0:
                    self.leveloned.__init__(self.screen, self.gameStateManager, self.clock)
                    pygame.mixer.stop()
                    self.death_song.play(-1)
                    self.gameStateManager.set_state('restartlev1a')
                elif len(self.leveloned.enemies) == 0 and x > 1800:
                    self.leveloned.__init__(self.screen, self.gameStateManager, self.clock)
                    pygame.mixer.stop()
                    self.gameStateManager.set_state('cutscene2')  ## adjust this to dev, switch to levelonea when done
                    self.cutscene2.start()
            elif current_state == 'leveltwoa':
                x = self.leveltwoa.original_x
                health = self.leveltwoa.gabby_health
                if health <= 0:
                    self.leveltwoa.__init__(self.screen, self.gameStateManager, self.clock)
                    pygame.mixer.stop()
                    self.death_song.play(-1)
                    self.gameStateManager.set_state('restartlev2a')
                elif len(self.leveltwoa.enemies) == 0 and x > 1800:
                    self.leveltwoa.__init__(self.screen, self.gameStateManager, self.clock)
                    self.gameStateManager.set_state('leveltwob')
                    pygame.mixer.fadeout(500)
                    self.array_music[1].play(-1)
                    self.leveltwob.setHealth(health)
            elif current_state == 'leveltwob':
                x = self.leveltwob.original_x
                health = self.leveltwob.gabby_health
                if health <= 0:
                    self.leveltwob.__init__(self.screen, self.gameStateManager, self.clock)
                    pygame.mixer.stop()
                    self.death_song.play(-1)
                    self.gameStateManager.set_state('restartlev2a')
                elif len(self.leveltwob.enemies) == 0 and x > 1800:
                    self.leveltwob.__init__(self.screen, self.gameStateManager, self.clock)
                    self.gameStateManager.set_state('leveltwoc')
                    self.leveltwoc.setHealth(health)
                    pygame.mixer.fadeout(500)
                    self.array_music[2].play(-1)
            elif current_state == 'leveltwoc':
                x = self.leveltwoc.original_x
                health = self.leveltwoc.gabby_health
                if health <= 0:
                    self.leveltwoc.__init__(self.screen, self.gameStateManager, self.clock)
                    pygame.mixer.stop()
                    self.death_song.play(-1)
                    self.gameStateManager.set_state('restartlev2a')
                elif len(self.leveltwoc.enemies) == 0 and x > 1800:
                    self.leveltwoc.__init__(self.screen, self.gameStateManager, self.clock)
                    pygame.mixer.fadeout(500)
                    self.gameStateManager.set_state('cutscene3')  ## adjust this to dev, switch to levelonea when done
                    self.cutscene3.start()
            elif current_state == 'leveltwod':
                x = self.leveltwod.original_x
                health = self.leveltwod.gabby_health
                if health <= 0:
                    self.leveltwod.__init__(self.screen, self.gameStateManager, self.clock)
                    pygame.mixer.stop()
                    self.death_song.play(-1)
                    self.gameStateManager.set_state('restartlev2a')
                elif len(self.leveltwod.enemies) == 0 and x > 1800:
                    self.leveltwod.__init__(self.screen, self.gameStateManager, self.clock)
                    pygame.mixer.fadeout(500)
                    self.gameStateManager.set_state('cutscene4')  ## adjust this to dev, switch to levelonea when done
                    self.cutscene4.start()

            # runs all of the important shit
            self.states[self.gameStateManager.get_state()].run(events, elapsed_time)
            pygame.display.update()


