import pygame
from OPTIONS import *
from Scene import Scene
from GameScene import GameScene
from Button import Button
from Text import Text

class MainScene(Scene):

    def __init__(self, display, skin=''):
        super().__init__(display)
        self.skin = skin
        if skin == '':
            self.skin = 'phoenix'
        self.item_list = [Text(self.display, "Flappy Phoenix", (SCREENINFO.WIDTH / 2 - 100 * 4.95, 144), 90, "assets/font.ttf", (0, 0, 0)),
                          Text(self.display, "Flappy Phoenix", (SCREENINFO.WIDTH / 2 - 100 * 4.90, 140), 90, "assets/font.ttf", (255, 0, 0)),
                          Button(self.display, (SCREENINFO.WIDTH / 2 - (SCREENINFO.WIDTH / 1920 * 1200) / 2 - 40, SCREENINFO.HEIGHT / 1080 * 500), (SCREENINFO.WIDTH / 1920 * 1200, SCREENINFO.HEIGHT / 1080 * 125), (255, 255, 255), (255, 0, 0), "PLAY", SET_GAMESCENE),
                          Button(self.display, (SCREENINFO.WIDTH / 2 - (SCREENINFO.WIDTH / 1920 * 1200) / 2 - 40, SCREENINFO.HEIGHT / 1080 * 700), (SCREENINFO.WIDTH / 1920 * 1200, SCREENINFO.HEIGHT / 1080 * 125), (255, 255, 255), (255, 0, 0), "QUIT", QUIT_GAME, 'assets/Arrow_back.png'),
                          Button(self.display, (SCREENINFO.WIDTH / 2 - (SCREENINFO.WIDTH / 1920 * 1200) / 2 + SCREENINFO.WIDTH / 1920 * 1200, SCREENINFO.HEIGHT / 1080 * 570), (100, 100), (255, 255, 255), (255, 0, 0), "", SET_SKINSELECT, f"assets/player/{self.skin}/pre.png")]
        self.set_background('assets/bg_depixelized_1920x1080.png')
        self.set_music("assets/theme.mp3")
        self.play_music()
        self.__konami = [pygame.K_UP, pygame.K_UP, pygame.K_DOWN, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_a, pygame.K_b]
        self.__konami_count = 0
        self.__usr_konami = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    def __is_konami(self, event):
        if event.type == pygame.KEYDOWN and event.key == self.__konami[self.__konami_count]:
            self.__usr_konami[self.__konami_count] = 1
            self.__konami_count += 1
        elif event.type == pygame.KEYDOWN and event.key != self.__konami[self.__konami_count]:
            self.__usr_konami = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            self.__konami_count = 0
        if self.__usr_konami == [1 for _ in range(10)]:
            return [SET_EASTEREGG]

    def update(self, event):
        if event == None:
            return
        retour = self.__is_konami(event)
        if retour != None:
            return retour
        return super().update(event)
