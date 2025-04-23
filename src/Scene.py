import pygame
from OPTIONS import *
from Sprite import Sprite

class Scene:
    """
    Cette classe permet de creer une scene
    """
    def __init__(self, display) -> None:
        self.display = display
        self.has_background = False
        self.item_list = []
        self.music = ''

    def update(self, event):
        if event == None:
            return None
        retour = []
        for item in self.item_list:
            if type(item).__name__ is 'Button':
                retour.append(item.update(event))
        return retour
    
    def re_init(self):
        self.__init__(self.display)

    def set_background(self, img:str):
        if self.has_background:
            self.item_list[0] = Sprite(self.display, img, (0,0), SCREENINFO.WIDTH, SCREENINFO.HEIGHT)
            return
        item_list = [Sprite(self.display, img, (0,0), SCREENINFO.WIDTH, SCREENINFO.HEIGHT)]
        for item in self.item_list:
            item_list.append(item)
        self.item_list = item_list
        self.has_background = True

    def draw(self):
        for item in self.item_list:
            item.draw()

    def undraw(self):
        for item in self.item_list:
            if type(item).__name__ is 'Button':
                item.undraw()
    
    def play_music(self):
        if self.music != '':
            pygame.mixer.music.load(self.music)
            pygame.mixer.music.play()

    def set_music(self, music_path:str):
        self.music = music_path

    def stop_music(self):
        pygame.mixer.music.stop()

    def pause_music(self):
        pygame.mixer.music.pause()

    def unpause_music(self):
        pygame.mixer.music.unpause()