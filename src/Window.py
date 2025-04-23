import pygame
from OPTIONS import *
from GameScene import GameScene
from MainScene import MainScene
from EasterEggScene import EasterEggScene
from SkinSelect import SkinSelect
from Video import Video


class Window:
    """
    Cette classe permet de creer la fenetre pygame associé au jeu
    """
    def __init__(self) -> None:
        pygame.init()
        pygame.mixer.init()
        if OPTIONS.SOUND_ON: pygame.mixer.music.set_volume(100.0)
        else: pygame.mixer.music.set_volume(0.0)
        if SCREENINFO.FULLSCREEN:
            self.display = pygame.display.set_mode((SCREENINFO.WIDTH, SCREENINFO.HEIGHT), pygame.FULLSCREEN)
        else : self.display = pygame.display.set_mode((SCREENINFO.WIDTH, SCREENINFO.HEIGHT))
        pygame.display.set_caption(" - Flappy Phoenix - Miami Bitch Team ", "assets/player/phoenix/pre.png")
        video = Video("assets/video/intro/frames/")
        video.add_sound("assets/video/intro/audio.mp3")
        video.play(self.display, (0, 0), SCREENINFO.WIDTH, SCREENINFO.HEIGHT)
        self.skin = 'phoenix'
        self.scene = MainScene(self.display, self.skin)
        self.clock = pygame.time.Clock()
        self.is_running = True
        self.list_skins = ['phoenix', 'easteregg']

    def set_running_false(self):
        self.is_running = False

    def run(self):
        while self.is_running:
            self.clock.tick(SCREENINFO.FPS)
            for event in pygame.event.get():
                self.update(event)
                if event.type == pygame.QUIT:
                    self.set_running_false()
            self.scene.draw()
            self.update(None)
            pygame.display.flip()
            self.refill()
        pygame.quit()

    def refill(self):
        self.display.fill((0, 0, 0))
    
    def update(self, event):
        """
        fonction update window
        """
        return_values = self.scene.update(event)
        if return_values == None:
            return
        for value in return_values:
            if value != None and value >= 0:
                self.scene.stop_music()
            if value == QUIT_GAME:
                self.set_running_false()
            if value == SET_GAMESCENE:
                self.scene = GameScene(self.display, self.skin)
            if value == SET_MAINSCENE:
                self.scene = MainScene(self.display, self.skin)
            if value == SET_EASTEREGG:
                self.scene = EasterEggScene(self.display)
            if value == SET_SKINSELECT:
                self.scene = SkinSelect(self.display)
            if value in INTER_SKINS:
                self.skin = self.list_skins[value - 10]